from django.contrib import admin

from blogs.models import blogs

#When we want to display selected fields
class blogAdmin(admin.ModelAdmin):
   list_display=('blog_title','blog_des','blog_date','blog_img','blog_slug')

admin.site.register(blogs,blogAdmin)

