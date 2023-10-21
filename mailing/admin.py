from django.contrib import admin

from mailing.models import MailingSettings, Mail, Client, Logs


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('status',
                    'topic_mail', 'body_mail',)
    list_filter = ('status',)




@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'status_send', 'last_attempt_send',)





