from django.urls import path
from . import views
urlpatterns = [
    path('',views.fankui_index),
    path('jianyi/',views.fankui_store),
   
    
]
