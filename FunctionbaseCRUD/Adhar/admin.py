from django.contrib import admin
from .models import Adharcard
# Register your models here.
class AdharcardAdmin(admin.ModelAdmin):
    list_display =['aid', 'aname', 'anumber', 'aadd']
admin.site.register(Adharcard, AdharcardAdmin)