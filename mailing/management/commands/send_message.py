from datetime import datetime, date

from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand
from mailing.models import MailingSettings, Logs
from mailing.services.services import install_next_date


class Command(BaseCommand):
    def handle(self, *args, **options):
        for mail in MailingSettings.objects.filter(status=MailingSettings.STATUS_STARTED):
            email_list = [x.email for x in mail.clients.all()]
            time_now = datetime.now()

            if mail.day == date.today() and mail.time <= time_now.time():
                try:
                    result = send_mail(
                        subject=mail.topic_mail,
                        message=mail.body_mail,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=email_list,
                        fail_silently=False
                    )

                    if result:
                        Logs.objects.create(mailing=mail,
                                            status_send='Успешно',
                                            last_attempt_send=datetime.now(),
                                            last_attempt_response='200'
                                            )

                        mail.day = install_next_date(mail)
                        mail.save()

                except Exception as error:
                    Logs.objects.create(mailing=mail,
                                        status_send='Ошибка',
                                        last_attempt_send=datetime.now(),
                                        last_attempt_response=error
                                        )