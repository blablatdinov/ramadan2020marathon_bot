from django.urls import path
from ramadan_marafon.settings import TG_BOT

from bot_init.views import bot


token = TG_BOT['TOKEN']
urlpatterns = [
    path(f'{token}', bot)
]