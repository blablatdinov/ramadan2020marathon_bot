from datetime import datetime

import pytz

from marathon.models import Book, Quran, Charging, SelfAnalyze


def check_inst(inst):
    utc = pytz.UTC
    ranges = [
        (datetime(2020, 4, 22), datetime(2020, 4, 23)),
        (datetime(2020, 4, 23), datetime(2020, 4, 24)),
        (datetime(2020, 4, 24), datetime(2020, 4, 25)),
        (datetime(2020, 4, 25), datetime(2020, 4, 26)),
        (datetime(2020, 4, 26), datetime(2020, 4, 27)),
        (datetime(2020, 4, 27), datetime(2020, 4, 28)),
        (datetime(2020, 4, 28), datetime(2020, 4, 29)),
        # (datetime(2020, 4, 30), datetime(2020, 4, 28)),
        # (datetime(2020, 4, 27), datetime(2020, 4, 28)),
    ]
    points = 0
    points_plus = 1
    for elem in ranges:
        qs = inst.objects.filter(
            datetime__gt=elem[0].replace(tzinfo=utc),
            datetime__lt=elem[1].replace(tzinfo=utc)
        )
        if qs.count():
            points += points_plus
            points_plus += 1
    return points


def stat(tg_chat_id):
    utc = pytz.UTC
    books = Book.objects.filter(subscriber__tg_chat_id=tg_chat_id)
    points_count = 0
    result = f'Очков за зарядку: {check_inst(Charging)}\n' \
             f'Очков за чтение Корана: {check_inst(Quran)}\n' \
             f'Очков за чтение книг: {check_inst(Book)}\n' \
             f'Очков за самоанализ: {check_inst(SelfAnalyze)}\n'
    return result
