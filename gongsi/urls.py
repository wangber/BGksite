from django.urls import path
from . import views
urlpatterns = [
    path('xingfukuaile',views.xingfukuaile),
    path('chongwuxiangqing<int:order>.html',views.chongwuxiangqing),
    path('allchongwu',views.allchongwu)
   
    
]

