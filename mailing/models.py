from datetime import datetime

from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """Клиент сервиса"""
    email = models.EmailField(unique=True, verbose_name='Почта')
    name = models.CharField(max_length=150, verbose_name='Фамилия Имя Отчество', **NULLABLE)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)


    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'



class Mail(models.Model):
    """Сообщение для рассылки"""
    topic_mail = models.CharField(max_length=100, verbose_name='Тема письма')
    body_mail = models.CharField(max_length=100, verbose_name='Тело письма')

    def __str__(self):
        return (f'{self.topic_mail} {self.body_mail}')

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class MailingSettings(models.Model):
    """Рассылка (настройки)"""

    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = (
        (PERIOD_DAILY, 'Ежедневная'),
        (PERIOD_WEEKLY, 'Раз в неделю'),
        (PERIOD_MONTHLY, 'Раз в месяц'),
    )

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'

    STATUSES = (
        (STATUS_STARTED, 'Запущена'),
        (STATUS_CREATED, 'Создана'),
        (STATUS_DONE, 'Завершена'),
    )

    period = models.CharField(max_length=20, choices=PERIODS, verbose_name='Периодичность рассылки',
                              default=PERIOD_DAILY)
    status = models.CharField(max_length=20, choices=STATUSES, verbose_name='Статус рассылки', default=STATUS_CREATED)
    time = models.TimeField(default=datetime.now, verbose_name="Время отправки")
    clients = models.ManyToManyField(Client, verbose_name='Клиент', **NULLABLE)
    day = models.DateField(default=datetime.today, verbose_name='Дата начала')
    topic_mail = models.CharField(default='',max_length=100, verbose_name='Тема письма')
    body_mail = models.CharField(default='', max_length=100, verbose_name='Тело письма')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return (f'{self.period} {self.status} {self.time},'
                f'{self.topic_mail} {self.body_mail}'
                f'{self.clients}')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    permissions = [
        ('set_status', 'Can change mailing status')
    ]


class Logs(models.Model):
    """Логи рассылки"""

    last_attempt_send = models.DateTimeField(default=None, verbose_name="Дата и время последней попытки")
    status_send = models.CharField(max_length=150, verbose_name='Статус попытки')
    mailing = models.ForeignKey('MailingSettings', on_delete=models.CASCADE,
                                verbose_name='Рассылка,которая отправлялась')

    last_attempt_response = models.CharField(max_length=150, **NULLABLE, verbose_name='Ответ почтового сервера')

    def __str__(self):
        return (f'{self.last_attempt_send} {self.status_send}'
                f'{self.mailing}')

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
