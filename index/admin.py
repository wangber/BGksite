from django.contrib import admin
from .models import members,happytime,activity,Loldata
admin.site.site_header = 'BGk小站后台管理系统'
admin.site.site_title = 'BGk小站后台管理系统'
admin.site.register(members)
admin.site.register(happytime)
admin.site.register(Loldata)
admin.site.register(activity)


# Register your models here.
