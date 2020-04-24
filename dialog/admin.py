from django.contrib import admin

from marathon.models import Charging, Quran, Book, SelfAnalyze

admin.site.register(Charging)
admin.site.register(Quran)
admin.site.register(Book)
admin.site.register(SelfAnalyze)
