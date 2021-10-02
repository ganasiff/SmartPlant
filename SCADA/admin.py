from django.contrib import admin

# Register your models here.
from .models import Settings

class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id','role','name','description']
    search_fields = ['id','role', 'name','description']

admin.site.register(Settings, SettingsAdmin)
