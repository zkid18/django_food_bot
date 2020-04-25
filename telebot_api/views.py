from django.shortcuts import render

import requests
import json
import telebot

from django.http import JsonResponse
from django.views import View
from django.conf import settings


# Create your views here.

TELEGRAM_URL = "https://api.telegram.org/bot"
BOT_TOKEN = settings.BOT_TOKEN


# https://api.telegram.org/botBOT_TOKEN?url=https://8ed39930.ngrok.io/bot/webhook

class BotView(View):
    tb = telebot.TeleBot(BOT_TOKEN)

    @tb.message_handler(content_types=['photo'])
    def handle_photo(self, message):
        print("Photo received")

    @tb.message_handler(commands=['help', 'start'])
    def send_welcome(self, message):
        self.tb.reply_to(message,   
                 ("Hi there, I am EchoBot.\n"
                  "I am here to echo your kind words back to you."))

    def post(self, request, *args, **kwargs):
        t_data = json.loads(request.body)
        update = telebot.types.Update.de_json(t_data)
        self.tb.process_new_messages([update.message])
        return ''
        # t_message = t_data["message"]
        # t_chat = t_message["chat"]

        # try:
        #     text = t_message["text"].strip().lower()
        # except Exception:
        #     return JsonResponse({"ok": "POST request processed"})

        # text = text.lstrip("/")
        # #self.send_message(text, t_chat["id"])
        # self.tb.send_message(t_chat["id"], text)
        # return JsonResponse({"ok": "POST request processed"})

    @staticmethod
    def send_message(message, chat_id):
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown",
        }
        requests.post(
            f"{TELEGRAM_URL}{BOT_TOKEN}/sendMessage", data=data
        )

