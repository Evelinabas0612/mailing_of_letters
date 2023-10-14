from django.contrib import admin

from mailing.models import MailingSettings, Mail, Client, Logs


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('time', 'period', 'status')
    list_filter = ('time',)
    search_fields = ('status',)


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('topic_mail', 'body_mail')
    search_fields = ('topic_mail',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('status_send',)


