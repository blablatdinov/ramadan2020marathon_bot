from telebot import types

from bot_init.utils import save_message
from bot_init.views import tbot, get_markup


def dialog(tg_chat_id):
    markup = get_markup('charge: yes', 'charge: no')
    msg = tbot.send_message(tg_chat_id, 'Сделали ли вы сегодня зарядку?', reply_markup=markup)
    save_message(msg)
    return None
    # markup = get_markup('quran: yes', 'quran: no')
    # msg = tbot.send_message(tg_chat_id, 'Прочитали ли вы сегодня джуз?', reply_markup=markup)
    # save_message(msg)
    # markup = get_markup('book: yes', 'book: no')
    # msg = tbot.send_message(tg_chat_id, 'Прочитали ли вы сегодня 20 страниц книги?', reply_markup=markup)
    # save_message(msg)
    # markup = get_markup('analyze: yes', 'analyze: no')
    # msg = tbot.send_message(tg_chat_id, 'Уделили ли вы вермя самоанализу?', reply_markup=markup)
    # save_message(msg)

