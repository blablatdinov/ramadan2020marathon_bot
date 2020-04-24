from django.db import models

from bot_init.models import Subscriber


class Charging(models.Model):
    subscriber = models.ForeignKey(Subscriber, related_name='chargings', on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    datetime = models.DateTimeField(blank=True, null=True)


class Quran(models.Model):
    subscriber = models.ForeignKey(Subscriber, related_name='qurans', on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    datetime = models.DateTimeField(blank=True, null=True, editable=True)


class Book(models.Model):
    subscriber = models.ForeignKey(Subscriber, related_name='books', on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    datetime = models.DateTimeField(blank=True, null=True, editable=True)


class SelfAnalyze(models.Model):
    subscriber = models.ForeignKey(Subscriber, related_name='self_analyze', on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    datetime = models.DateTimeField(blank=True, null=True, editable=True)
