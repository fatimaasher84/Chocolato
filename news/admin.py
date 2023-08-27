from django.contrib.admin.sites import site
from django.contrib import admin
from news.models import news
# Register your models here.

class newsAdmin(admin.ModelAdmin):
    list_display=("news_title","news_desc")

admin.site.register(news,newsAdmin)