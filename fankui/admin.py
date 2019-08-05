from django.contrib import admin
from .models import jianyi
class JianyiAdmin(admin.ModelAdmin):
    list_display = ('content','ider',)
admin.site.register(jianyi,JianyiAdmin)

# Register your models here.
