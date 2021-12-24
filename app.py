import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "start", "menu", "introduce", "bank", "value", "value_now", "show_value_now", "value_recently", "value_3month", "show_value_3month", "value_1month", "show_value_1month"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "start",
            "conditions": "is_going_to_start",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "introduce",
            "conditions": "is_going_to_introduce",
        },
        {
            "trigger": "advance",
            "source": "introduce",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "bank",
            "conditions": "is_going_to_bank",
        },
        {
            "trigger": "advance",
            "source": "bank",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "bank",
            "dest": "value",
            "conditions": "is_going_to_value",
        },
        {
            "trigger": "advance",
            "source": "value",
            "dest": "bank",
            "conditions": "is_going_to_bank",
        },
        {
            "trigger": "advance",
            "source": "value",
            "dest": "value_now",
            "conditions": "is_going_to_value_now",
        },
        {
            "trigger": "advance",
            "source": "value",
            "dest": "value_recently",
            "conditions": "is_going_to_value_recently",
        },
        {
            "trigger": "advance",
            "source": "value",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "value_now",
            "dest": "show_value_now",
            "conditions": "is_going_to_show_value_now",
        },
        {
            "trigger": "advance",
            "source": "show_value_now",
            "dest": "value_now",
            "conditions": "is_going_to_value_now",
        },
        {
            "trigger": "advance",
            "source": "value_now",
            "dest": "value",
            "conditions": "is_going_to_value",
        },
        {
            "trigger": "advance",
            "source": "value_recently",
            "dest": "value",
            "conditions": "is_going_to_value",
        },
        {
            "trigger": "advance",
            "source": "value_recently",
            "dest": "value_3month",
            "conditions": "is_going_to_value_3month",
        },
        {
            "trigger": "advance",
            "source": "value_recently",
            "dest": "value_1month",
            "conditions": "is_going_to_value_1month",
        },
        {
            "trigger": "advance",
            "source": "value_3month",
            "dest": "value_recently",
            "conditions": "is_going_to_value_recently",
        },
        {
            "trigger": "advance",
            "source": "value_1month",
            "dest": "value_recently",
            "conditions": "is_going_to_value_recently",
        },
        {
            "trigger": "advance",
            "source": "value_1month",
            "dest": "show_value_1month",
            "conditions": "is_going_to_show_value_1month",
        },
        {
            "trigger": "advance",
            "source": "value_3month",
            "dest": "show_value_3month",
            "conditions": "is_going_to_show_value_3month",
        },
        {
            "trigger": "advance",
            "source": "show_value_3month",
            "dest": "value_3month",
            "conditions": "is_going_to_value_3month",
        },
        {
            "trigger": "advance",
            "source": "show_value_1month",
            "dest": "value_1month",
            "conditions": "is_going_to_value_1month",
        },
        {"trigger": "go_back", "source": ["start", "menu", "introduce", "bank", "value", "value_now", "show_value_now", "value_recently", "value_3month", "show_value_3month", "value_1month", "show_value_1month"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
