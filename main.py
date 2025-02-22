from dotenv import load_dotenv
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)
import os

from src.chatgpt import ChatGPT, DALLE
from src.models import OpenAIModel
from src.memory import Memory
from src.logger import logger

load_dotenv('.env')

app = Flask(__name__)
line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

models = OpenAIModel(api_key=os.getenv('OPENAI_API'), model_engine=os.getenv('OPENAI_MODEL_ENGINE'))

memory = Memory(system_message=os.getenv('SYSTEM_MESSAGE'))
chatgpt = ChatGPT(models, memory)
dalle = DALLE(models)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    user_id = event.source.user_id
    text = event.message.text
    logger.info(f'{user_id}: {text}')
    if text.startswith('/產生圖片'):
        response = dalle.generate(text[5:].strip())
        msg = ImageSendMessage(
            original_content_url=response,
            preview_image_url=response
        )
    elif text.startswith('/清除對話'):
        chatgpt.clean_history(user_id)
        msg = TextSendMessage(text="喵洽什麼都不記得囉")
    else:
        response = chatgpt.get_response(user_id, text)
        response = response_preprocessing(response)
        msg = TextSendMessage(text=response)

    line_bot_api.reply_message(
        event.reply_token,
        msg
        )

# 對 gpt 的回應做預處理
def response_preprocessing(response: str):

    # 消除開發人員提示
    print(response)
    d_string = 'Developer Mode Output'
    if d_string in response:
        print('remove Developer')
        d_start = response.find(d_string)
        new_response = response[d_start + len(d_string) + 2:]
    else:
        new_response = response

    return new_response

@app.route("/", methods=['GET'])
def home():
    return 'Hello World'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
