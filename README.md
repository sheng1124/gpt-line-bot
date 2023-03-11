# ChatGPT Line Bot

## 介紹
* 在 Line 中去導入 ChatGPT Bot，只要在輸入框直接輸入文字，即可與 ChatGPT 開始互動，除了 ChatGPT 以外，也直接串上了 DALL·E 2 的模型，輸入 `/產生圖片 + 文字`，就會回傳相對應的圖片，如下圖所示：
    * ![](https://i.imgur.com/pYcQ3wg.jpg)
    * ![](https://i.imgur.com/AZvdYj6.jpg)




## 安裝步驟
* [參考教學](https://github.com/TheExplainthis/ChatGPT-Line-Bot)

## 本地部屬
1. 創建 .env 文件
2. 編輯 .env 文件
    ![](https://i.imgur.com/ZHkF64b.png)
3. 前往 [ngrok](https://dashboard.ngrok.com/get-started/setup) 網域代理服務
4. 安裝 ngrok 丟到主目錄
5. 認證帳戶 & 授權
    * ```ngrok config add-authtoken ...```
6. 啟用端口 8080 
    * ```ngrok http 8080```
7. 複製 端口對應網址
    * ![](https://i.imgur.com/PJ0IVS1.png)
8. 編輯 linebot webhook settings
    * ![](https://i.imgur.com/y9y4KUr.png)



## 指令
在文字輸入框中直接輸入文字，即可與 ChatGPT 開始對話，而其他指令如下：

| 指令 | 說明 |
| --- | ----- |
| `/產生圖片` | 在輸入框輸入 `/產生圖片` + 文字，就會調用 DALL·E 2 模型，即可生成圖像。|
| `/清除對話` | 在輸入框輸入 `/清除對話` 即會清空 chat gpt 紀錄的對話。|

## 參考資料
- [ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)
- [gpt-ai-assistant](https://github.com/memochou1993/gpt-ai-assistant)
- [ChatGPT-Discord-Bot](https://github.com/TheExplainthis/ChatGPT-Discord-Bot)
