from django.db import models
from autoslug import AutoSlugField
import datetime
from tinymce.models import HTMLField

#class DummyUser(models.Model):
 #   pass

class blogs(models.Model):
    blog_title=models.CharField(max_length=100)
    blog_des=HTMLField()
    #To add now date we can also use models.DateField(auto_now_add=True)
    blog_date=models.DateField(null=True,default=datetime.date.today)
    blog_img=models.FileField(upload_to="blimages/",max_length=250,null=True,default=None)
    blog_author=models.CharField(max_length=50,null=True)
    blog_slug=AutoSlugField(populate_from='blog_title',unique=True,null=True,default=None)
    #To add like button to blogposts,it can be many likes so we use ManyToManyField and related_name is sort of foreign key 
#    blog_likes=models.ManyToManyField(DummyUser, through='BlogLikes',related_name='blog_posts')

#class BlogLikes(models.Model):
 #   blog=models.ForeignKey('blogs',on_delete=models.CASCADE)
  #  user=models.ForeignKey(DummyUser,on_delete=models.CASCADE)
