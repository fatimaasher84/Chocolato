from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class choco(models.Model):
    ch_title=models.CharField(max_length=50)
    ch_price=models.CharField(max_length=50)
    ch_des=HTMLField()
    #max_length will tell the url length of image,dafault value =None and null value can also be in this field
    ch_image=models.FileField(upload_to="chimages/",max_length=250,null=True,default=None)#upload_to will tell the folder in which images are uploaded in media folder 
    ch_slug=AutoSlugField(populate_from='ch_title',unique=True,null=True,default=None)

