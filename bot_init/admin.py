from django.contrib import admin

from bot_init.models import Subscriber, Message, Admin


class MessageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'json')
    search_fields = ('json', )


admin.site.register(Subscriber)
admin.site.register(Message, MessageAdmin)
admin.site.register(Admin)
