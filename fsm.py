import os
from transitions.extensions import GraphMachine
import message_shape
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
from utils import send_text_message, send_button_message, send_image_message
import pandas as pd

bank_url = {
        "台灣銀行" : "https://rate.bot.com.tw/"
        }
method_url = {
        "value_now" : "xrt?Lang=zh-TW",
        "value_recently" : "xrt/quote/ltm"
        }
def get_currency_now(web_address):
    res = pd.read_html(web_address+method_url["value_now"])
    df = res[0].iloc[:,:5]
    currency = df
    currency.columns=[u"幣別",u"現金買入",u"現金賣出",u"即期買入",u"即期賣出"]
    currency[u'幣別']=currency[u'幣別'].str.extract('\((\w+)\)')
    currency['幣別'].replace(" ", "");
    currency = pd.DataFrame(data = currency)
    return currency

class TocMachine(GraphMachine):
    bank = ''
    currency_type = ''
    currency_now = []
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_start(self, event):
        text = event.message.text
        return text.lower() == "start"

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"

    def on_enter_start(self, event):
        print("go to start finish\n");
        reply_token = event.reply_token
        message = message_shape.init_menu
        message_to_reply = FlexSendMessage("go to start", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_menu(self, event):
        print("go to menu finish\n");
        reply_token = event.reply_token
        message = message_shape.main_menu
        message_to_reply = FlexSendMessage("go to menu", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def is_going_to_introduce(self, event):
        text = event.message.text
        return text.lower() == "introduce"

    def on_enter_introduce(self, event):
        print("go to introduce finish\n");
        reply_token = event.reply_token
        message = message_shape.introduce_box
        message_to_reply = FlexSendMessage("go to introduce", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def is_going_to_bank(self, event):
        text = event.message.text
        return text.lower() == "bank"

    def on_enter_bank(self, event):
        print("go to bank finish\n");
        reply_token = event.reply_token
        message = message_shape.bank_select
        message_to_reply = FlexSendMessage("go to select bank", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def is_going_to_value(self, event):
        global bank
        text = event.message.text
        if text in ["台灣銀行"]:
            bank = text
        return text in ["台灣銀行", "value"] and bank in ["台灣銀行"]

    def on_enter_value(self, event):
        global bank
        global currency_now
        currency_now = get_currency_now(bank_url[bank])
        reply_token = event.reply_token
        message = message_shape.display_method
        message_to_reply = FlexSendMessage("go to select display method", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def is_going_to_value_now(self, event):
        text = event.message.text
        return text.lower() == "value_now"

    def on_enter_value_now(self, event):
        reply_token = event.reply_token
        message = message_shape.Currency_select_for_value_now
        message_to_reply = FlexSendMessage("go to Currency_select_for_value_now", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def is_going_to_value_recently(self, event):
        text = event.message.text
        return text.lower() == "value_recently"

    def on_enter_value_recently(self, event):
        reply_token = event.reply_token
        message = message_shape.value_recently
        message_to_reply = FlexSendMessage("go to value_recently"  , message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def is_going_to_show_value_now(self, event):
        text = event.message.text
        global currency_now
        global currency_type
        currency_type = text
        i = 0
        while currency_now["幣別"][i] != text :
            i+=1
            if(i == currency_now.shape[0]) :
                return False
        return True

    def on_enter_show_value_now(self, event):
        global currency_type
        global currency_now
        global bank
        reply_token = event.reply_token
        message = message_shape.show_value_now

        i = 0
        while currency_now["幣別"][i] != currency_type :
            i+=1

        message["body"]["contents"][2]["contents"][1]["text"] = bank
        message["body"]["contents"][3]["contents"][1]["text"] = currency_type
        message["body"]["contents"][5]["contents"][1]["text"] = currency_now['現金買入'][i]
        message["body"]["contents"][6]["contents"][1]["text"] = currency_now['現金賣出'][i]
        message["body"]["contents"][8]["contents"][1]["text"] = currency_now['即期買入'][i]
        message["body"]["contents"][9]["contents"][1]["text"] = currency_now['即期賣出'][i]

        message_to_reply = FlexSendMessage("go to show_value_now", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def is_going_to_value_3month(self, event):
        text = event.message.text
        return text.lower() == "value_3month"

    def on_enter_value_3month(self, event):
        reply_token = event.reply_token
        message = message_shape.select_currency_value_recently
        message_to_reply = FlexSendMessage("go to value_3month", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def is_going_to_show_value_1month(self, event):
        text = event.message.text
        return text.lower() == "go to show value 1month"

    def is_going_to_show_value_3month(self, event):
        text = event.message.text
        return text.lower() == "go to show value 3month"

    def is_going_to_value_1month(self, event):
        text = event.message.text
        return text.lower() == "value_1month"

    def on_enter_value_1month(self, event):
        reply_token = event.reply_token
        message = message_shape.select_currency_value_recently
        message_to_reply = FlexSendMessage("go to value_1month", message)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, message_to_reply)

