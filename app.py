from flask import Flask, request
import antolib
from linebot import (
    LineBotApi, WebhookHandler,
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError,
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

line_bot_api = LineBotApi('Ke4AD7dO7T4uy2KuNUueCSpwn4ja4UbM8oFPXz9ybpFjy9j7igeFF1l0V1f1p7jUEZTO3xGU+rsRJUiZOZ/GYJKB/NGFPQxLxXZ+rGeD8LFzNuGGLY7927r3vKg0jfFLmr5Hqtu0XQs3F7jPeMJjIAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('81e34f59d8adaa8a293a5b37cebe0c74')

app = Flask(__name__)

# username of anto.io account
user = 'sun_IN_moon'
# key of permission, generated on control panel anto.io
key = 'tZlbFUDeFGiTmSxQEjm3PaOdtQM7g024mJOuYp64'
# your default thing.
thing = 'Messaging'

anto = antolib.Anto(user, key, thing)


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
    message = event.message.text
     if(message == 'button1 on'):
        anto.pub('button1', 1)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Turn On button1"))
    elif(message == 'button1 off'):
        anto.pub('button1', 0)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Turn Off channel1"))
    elif(message == 'button2 on'):
        anto.pub('button2', 1)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Turn On button2"))
                         elif(message == 'button2 off'):
        anto.pub('button2', 0)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Turn Off button2"))

if __name__ == "__main__":
    anto.mqtt.connect()
    app.run(debug=True)
