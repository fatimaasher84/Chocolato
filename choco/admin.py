from django.contrib import admin

from choco.models import choco

class chocoAdmin(admin.ModelAdmin):
    list_display=('ch_title','ch_price','ch_des','ch_image')

admin.site.register(choco,chocoAdmin)
