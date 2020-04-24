from __future__ import absolute_import, unicode_literals
from bot_init.utils import save_message
from bot_init.views import tbot, get_markup
# Create your tasks here

from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab
from datetime import timedelta
from bot_init.models import Subscriber


@periodic_task(run_every=(crontab(hour=20, minute=0)), name='dialog')
#@periodic_task(run_every=(timedelta(seconds=5)), name='dialog')
def dialog():
    subs = Subscriber.objects.all()
    print(subs)
    markup = get_markup('charge: yes', 'charge: no')
    for sub in subs:
        try:
            msg = tbot.send_message(sub.tg_chat_id, 'Сделали ли вы сегодня зарядку?', reply_markup=markup)
            save_message(msg)
        except:
            pass

