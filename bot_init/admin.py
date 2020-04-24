from django.contrib import admin

from bot_init.models import Subscriber, Message, Admin

admin.site.register(Subscriber)
admin.site.register(Message)
admin.site.register(Admin)
