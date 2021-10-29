"""
1. 註冊line機器人 # google line messaging api
2. 建立GitHub專案
3. 安裝套件 + 使用範例程式碼  # SDK: software development kit 官方釋出SDK讓使用者與其產品互動
						    # webhook: 聊天機器人收到訊息立刻轉載給我們的程式
4. 註冊Heroku帳號
5. 安裝Heroku CLI + 建立專案
6. 上傳程式碼至Heroku
7. 把網址貼到line機器人設定
8. 開始回覆訊息
9. 回覆貼圖
10. 結語

"""
# web app usually name app.py
# python 架設伺服器 (即寫網站)最主流的兩個套件：flask(小規模/無畫面), django(大規模/有畫面)

from flask import Flask, request, abort # 用flask架設伺服器

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, 
)

app = Flask(__name__)

line_bot_api = LineBotApi('XAtdeXAibpWMmW6GwxwbhmOSvc+SlT2R0RhuFVvHhmgH8xTq8LlUBQZW052UzY1UfZ0Ltq5T2wTrCc/GjRt5vgvmrlwg1jae1NR/vz+4YICS0iR2Oa427JGCkEk5pJWK4ItieCSKgqUL5JS0+hqs3wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('218d24ac03c7444638b8f9d4a57a1696')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()