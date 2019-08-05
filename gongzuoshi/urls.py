from django.urls import path
from . import views
urlpatterns = [
    path('',views.gongzuoshi_index),
    path('seevideo-<int:order>.html',views.seevideo),
    path('videotype-<int:order>',views.videotype),
   
    
]
