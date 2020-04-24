from django.db import models


class Subscriber(models.Model):
    """ Модель подписчика """
    tg_chat_id = models.IntegerField()

    def __str__(self):
        return f'{self.tg_chat_id}'


class Admin(models.Model):
    sub = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    is_spam = models.BooleanField(default=False)

    def change_mode(self):
        self.is_spam = not self.is_spam
        self.save()

    def get_spam_status(self):
        if self.is_spam:
            return 'Режим рассылки включен'
        else:
            return 'Режим рассылки выключен'


class Message(models.Model):
    """ Сообщение """
    message_id = models.IntegerField()
    chat_id = models.IntegerField()
    json = models.TextField()
    comment = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return str(self.message_id)

    class Meta:
        verbose_name = 'Сообщеине'
        verbose_name_plural = 'Сообщения'
