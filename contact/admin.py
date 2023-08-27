from django.contrib import admin

from contact.models import contactEnquiry
from contact.models import newsletterModel

class contactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','message')

class newsletterAdmin(admin.ModelAdmin):
    list_display=('id','newsEmail')

admin.site.register(newsletterModel,newsletterAdmin)

admin.site.register(contactEnquiry,contactAdmin)