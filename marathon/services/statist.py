from datetime import datetime

import pytz

from marathon.models import Book, Quran, Charging, SelfAnalyze
from bot_init.models import Subscriber


def check_inst(inst, sub):
    utc = pytz.timezone('Europe/Moscow')
    ranges = [
        (datetime(2020, 4, 22, 3), datetime(2020, 4, 23, 3)),
        (datetime(2020, 4, 23, 3), datetime(2020, 4, 24, 3)),
        (datetime(2020, 4, 24, 3), datetime(2020, 4, 25, 3)),
        (datetime(2020, 4, 25, 3), datetime(2020, 4, 26, 3)),
        (datetime(2020, 4, 26, 3), datetime(2020, 4, 27, 3)),
        (datetime(2020, 4, 27, 3), datetime(2020, 4, 28, 3)),
        (datetime(2020, 4, 28, 3), datetime(2020, 4, 29, 3)),
        (datetime(2020, 4, 29, 3), datetime(2020, 4, 30, 3)),
        (datetime(2020, 4, 30, 3), datetime(2020, 5, 1, 3)),
        (datetime(2020, 5, 1, 3), datetime(2020, 5, 2, 3)),
        (datetime(2020, 5, 2, 3), datetime(2020, 5, 3, 3)),
        (datetime(2020, 5, 3, 3), datetime(2020, 5, 4, 3)),
        (datetime(2020, 5, 4, 3), datetime(2020, 5, 5, 3)),
        (datetime(2020, 5, 5, 3), datetime(2020, 5, 6, 3)),
        (datetime(2020, 5, 6, 3), datetime(2020, 5, 7, 3)),
    ]
    points = 0
    points_plus = 1
    for elem in ranges:
        qs = inst.objects.filter(
            subscriber=sub,
            status=True,
            datetime__gt=elem[0].replace(tzinfo=utc),
            datetime__lt=elem[1].replace(tzinfo=utc)
        )
        if qs.count():
            points += points_plus
            points_plus += 1
        else:
            points_plus = 1
    return points


def stat(tg_chat_id):
    utc = pytz.UTC
    sub = Subscriber.objects.get(tg_chat_id=tg_chat_id)
    books = Book.objects.filter(subscriber=sub)
    points_count = 0
    result = f'Очков за зарядку: {check_inst(Charging, sub)}\n' \
             f'Очков за чтение Корана: {check_inst(Quran, sub)}\n' \
             f'Очков за чтение книг: {check_inst(Book, sub)}\n' \
             f'Очков за самоанализ: {check_inst(SelfAnalyze, sub)}\n'
    return result
