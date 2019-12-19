#SDK software development kit 
# 軟體給硬體所做使用的 
# 所以要先下載line的ＳＤＫ用它寫好的東西繼續編輯程式
#  下面為開發網頁程式碼 

from flask import Flask, request, abort

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

line_bot_api = LineBotApi('509tKzyYfw+mm5pQcwOK+j6GEGRe9JKp+xwh8Vzw98dv1wCtNQFvScO9kmi/XL1A+LwfpuRnCEo6er1pjMQSvz3xXc4tsqq0CdkzBF0xWdxaxypgYRnXDwYWdyUPBOcxP0HGGeHv402Opq8wyWfYrgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('495bac6b7496ea5919459c6e165a3b77')


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
