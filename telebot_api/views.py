from django.shortcuts import render

import requests
import json
import telebot

from django.http import JsonResponse
from django.views import View
from django.conf import settings

from posts.models import Post

TELEGRAM_URL = settings.TELEGRAM_URL
BOT_TOKEN = settings.BOT_TOKEN

tb = telebot.TeleBot(BOT_TOKEN, threaded=False)

class BotView(View):

    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        update = telebot.types.Update.de_json(json_data)
        tb.process_new_messages([update.message])
        return JsonResponse({"ok": "POST request processed"})


@tb.message_handler(content_types=['photo'])
def handle_photo(message):
    image = tb.get_file(message.photo[-1].file_id)
    # post = Post(image=image, description="photo_insta")
    # post.save()
    print("Photo received")

@tb.message_handler(commands=['help', 'start'])
def send_welcome(message):
    tb.reply_to(message,   
                ("Hi there, I am EchoBot.\n"
                "I am here to echo your kind words back to you."))

@tb.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    tb.reply_to(message, message.text)