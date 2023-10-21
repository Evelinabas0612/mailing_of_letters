from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(verbose_name='Cодержимое')
    image = models.ImageField(upload_to='blogs/', verbose_name='Изображение', **NULLABLE)
    date_of_creation = models.DateField(verbose_name='Дата создания', auto_now_add=True, **NULLABLE)
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'