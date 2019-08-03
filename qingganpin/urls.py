from django.urls import path
from . import views
urlpatterns = [
    
    path('allmusic/',views.seeallmusic),
    path('seeallwenarticle/',views.seeallarticle)
    
]
