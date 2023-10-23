from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = models.CharField(max_length=35, verbose_name='имя', **NULLABLE)

    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    #avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    email_verify = models.BooleanField(default=False)
    # token = models.CharField(max_length=200, verbose_name='токен', **NULLABLE)
    # created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания токена', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # def create_superuser(self, username=None, email=None, password=None, **extra_fields):
    #     extra_fields.setdefault("is_staff", True)
    #     extra_fields.setdefault("is_superuser", True)
    #
    #     if extra_fields.get("is_staff") is not True:
    #         raise ValueError("Superuser must have is_staff=True.")
    #     if extra_fields.get("is_superuser") is not True:
    #         raise ValueError("Superuser must have is_superuser=True.")
    #
    #     return self.create_user(username, email, password, **extra_fields)




