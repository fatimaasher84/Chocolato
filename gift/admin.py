from django.contrib import admin
from gift.models import giftModel

# Register your models here.
class giftAdmin(admin.ModelAdmin):
    list_display=('gt_title','gt_price','gt_des','gt_image')

admin.site.register(giftModel,giftAdmin)