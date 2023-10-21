# Generated by Django 4.2.6 on 2023-10-21 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Фамилия Имя Отчество')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_attempt_send', models.DateTimeField(default=None, verbose_name='Дата и время последней попытки')),
                ('status_send', models.CharField(max_length=150, verbose_name='Статус попытки')),
                ('last_attempt_response', models.CharField(blank=True, max_length=150, null=True, verbose_name='Ответ почтового сервера')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_mail', models.CharField(max_length=100, verbose_name='Тема письма')),
                ('body_mail', models.CharField(max_length=100, verbose_name='Тело письма')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
            },
        ),
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('daily', 'Ежедневная'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], default='daily', max_length=20, verbose_name='Периодичность рассылки')),
                ('status', models.CharField(choices=[('started', 'Запущена'), ('created', 'Создана'), ('done', 'Завершена')], default='created', max_length=20, verbose_name='Статус рассылки')),
                ('time', models.TimeField(default=datetime.datetime.now, verbose_name='Время отправки')),
                ('day', models.DateField(default=datetime.datetime.today, verbose_name='Дата начала')),
                ('topic_mail', models.CharField(default='', max_length=100, verbose_name='Тема письма')),
                ('body_mail', models.CharField(default='', max_length=100, verbose_name='Тело письма')),
                ('clients', models.ManyToManyField(blank=True, null=True, to='mailing.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
    ]
