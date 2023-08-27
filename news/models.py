from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class news(models.Model):
    news_title=models.CharField(max_length=100)
    news_desc=HTMLField()
    news_date = models.DateField(null=True)
    news_phone=models.IntegerField(null=True)
    news_slug=AutoSlugField(populate_from='news_title',unique=True,null=True,default=None)