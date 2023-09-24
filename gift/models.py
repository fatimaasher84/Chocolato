from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.
class giftModel(models.Model):
    gt_title=models.CharField(max_length=50)
    gt_price=models.CharField(max_length=50)
    gt_des=HTMLField()
    gt_image=models.FileField(upload_to="gtimages/",max_length=250,null=True,default=None)#upload_to will tell the folder in which images are uploaded in media folder 
    gt_slug=AutoSlugField(populate_from='gt_title',unique=True,null=True,default=None)