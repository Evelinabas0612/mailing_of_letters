from datetime import timedelta

from django.core.cache import cache

from blog.models import Blog
from config import settings
from mailing.models import MailingSettings


def install_next_date(mail: MailingSettings):
    if mail.period == mail.PERIOD_DAILY:
        mail.day += timedelta(1)
    elif mail.period == mail.PERIOD_WEEKLY:
        mail.day += timedelta(7)
    else:
        mail.day += timedelta(30)
    return mail.day


def get_cached_blog():
    key = 'blog'
    quryset = Blog.objects.all()

    if settings.CACHE_ENABLED:
        blog_list = cache.get(key)
        if blog_list is None:
            blog_list = quryset
            cache.set(key, blog_list)
        return blog_list
    return quryset