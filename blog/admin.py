from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_of_creation',)
    list_filter = ('title', 'date_of_creation',)
