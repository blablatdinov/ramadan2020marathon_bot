from datetime import datetime
from time import sleep

import pytz
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.utils.timezone import make_aware
from django.views.decorators.csrf import csrf_exempt
from telebot import types

from bot_init.models import Subscriber, Admin, Message
from bot_init.utils import save_message
from marathon.models import Charging, Quran, Book, SelfAnalyze
from marathon.services.statist import stat
from ramadan_marafon.settings import TG_BOT

import telebot

API_TOKEN = TG_BOT['TOKEN']
WEBHOOK_URL = TG_BOT['WEBHOOK_SITE']

tbot = telebot.TeleBot(API_TOKEN)
tbot.remove_webhook()
sleep(0.1)
tbot.set_webhook(f'{WEBHOOK_URL}/{API_TOKEN}')

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button = types.KeyboardButton('Статистика')
keyboard.row(button)


def stop_retry(func):

    def wrapper(message):
        #if message.chat.id == 358610865:
        if Message.objects.filter(message_id=message.message_id):
            print('reply')
            #return tbot.send_message(message.chat.id,'Привет, админ')
            return ''
        return func(message)

    return wrapper


@csrf_exempt
def bot(request):
    if request.content_type == 'application/json':
        json_data = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_data)
        tbot.process_new_updates([update])
        return HttpResponse('')

    else:
        raise PermissionDenied


@tbot.message_handler(commands=['start'])
@stop_retry
def start(message):
    save_message(message)
    Subscriber.objects.get_or_create(tg_chat_id=message.chat.id)
    print(message.chat.id)
    msg = tbot.send_message(message.chat.id, 'Стартовое сообщение', reply_markup=keyboard)
    save_message(msg)


@tbot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', 'text'])
@stop_retry
def admin_spam(message):
    save_message(message)
    if message.chat.id in TG_BOT['admins']:
        admin = Admin.objects.get(sub__tg_chat_id=message.chat.id)
        if message.text == '/subs':
            msg = tbot.send_message(message.chat.id, Subscriber.objects.all().count())
            save_message(msg)
        if admin.is_spam and message.text != '/spam':
            for sub in Subscriber.objects.all():
                try:
                    msg = tbot.forward_message(sub.tg_chat_id, message.chat.id, message.message_id)
                    save_message(msg)
                except:
                    pass
        if message.text == '/spam':
            admin.change_mode()
            msg = tbot.send_message(message.chat.id, admin.get_spam_status(), reply_markup=keyboard)
            save_message(msg)
            return None

    if message.chat.id not in TG_BOT['admins']:
        print('wow')

    if message.text == 'Статистика':
        text = stat(message.chat.id)
        msg = tbot.send_message(message.chat.id, text, reply_markup=keyboard)
        save_message(msg)


def get_markup(cal1, cal2):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Да', callback_data=cal1)
    button2 = types.InlineKeyboardButton(text='Нет', callback_data=cal2)
    return markup.row(button1, button2)


@tbot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    tg_chat_id = call.from_user.id
    data = str(call.data).split(' ')
    sub = Subscriber.objects.get(tg_chat_id=tg_chat_id)
    #call.message.date = 1588073904
    if 'charge' in data[0]:
        date = make_aware(datetime.fromtimestamp(call.message.date))
        status = True if data[1] == 'yes' else False
        Charging.objects.create(subscriber=sub, datetime=date, status=status)
        markup = get_markup('quran: yes', 'quran: no')
        msg = tbot.send_message(tg_chat_id, 'Прочитали ли вы сегодня джуз?', reply_markup=markup)
        save_message(msg)
    elif 'quran' in data[0]:
        date = make_aware(datetime.fromtimestamp(call.message.date))
        status = True if data[1] == 'yes' else False
        Quran.objects.create(subscriber=sub, datetime=date, status=status)
        markup = get_markup('book: yes', 'book: no')
        msg = tbot.send_message(tg_chat_id, 'Прочитали ли вы сегодня 20 страниц книги', reply_markup=markup)
        save_message(msg)
    elif 'book' in data[0]:
        date = make_aware(datetime.fromtimestamp(call.message.date))
        status = True if data[1] == 'yes' else False
        Book.objects.create(subscriber=sub, datetime=date, status=status)
        markup = get_markup('analyze: yes', 'analyze: no')
        msg = tbot.send_message(tg_chat_id, 'Уделили ли вы время самоанализу', reply_markup=markup)
        save_message(msg)
    elif 'analyze' in data[0]:
        sub = Subscriber.objects.get(tg_chat_id=call.from_user.id)
        date = make_aware(datetime.fromtimestamp(call.message.date))
        status = True if data[1] == 'yes' else False
        SelfAnalyze.objects.create(subscriber=sub, datetime=date, status=status)

    tbot.delete_message(call.from_user.id, call.message.message_id)
