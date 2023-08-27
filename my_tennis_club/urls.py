"""
URL configuration for my_tennis_club project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#Import views from the app i have created
from my_tennis_club import views
#import these two libraries to upload media files in admin site to show on my webpage
from django.conf import settings
from django.conf.urls.static import static #static is a function which will allow media to be used with the urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage,name='index'),
    path('about/',views.aboutus,name='about'),
    path('chocolates/',views.chocolates,name='chocolates'),
    #<int,str,slug types can be used for courseid>
    path('gift/',views.gift,name="gift"),
    path('blg/',views.blg,name="blg"),
    path('contact/',views.contact,name='contact'),
    path('delivery/',views.delivery,name='delivery'),
    path('shop/',views.shop,name="shop"),
    path('trade/',views.trade,name="trade"),
    path('newsletter/',views.newsletter,name='newsletter'),
    path('tinymce/', include('tinymce.urls')),
    path('submitform/',views.submitform,name='submitform'),
    path('newsDetail/<slug>',views.newsDetail),
    path('blogDetails/<slug>',views.blogDetails,name='blogDetails'),
    path('chocodetails/<slug>',views.chocodetails,name='chocodetails'),
    path('giftdetails/<slug>',views.giftdetails,name='giftdetails'),
#    path('likePost/<int:id>',views.LikeView,name='likePost'),
]


#We will check whether DEBUG is true in settings.py or not
if settings.DEBUG:
    #if debug is True then we will concatenate the value(MEDIA_URL from settings.py and save MEDIA_ROOT from settings.py in document_root)with the urlpatterns
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)