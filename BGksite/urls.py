"""BGksite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from django.views.static import serve
from index import views as index_view
from index.views import activity_intrudce, member_intruduce
from daysentence import views as daysentence_view
from disanketang.views import disanketang_index
from qingganpin.views import qingganpin_index,seeqinggan,tolisen
from gongsi.views import gongsi_index
from .settings import MEDIA_ROOT
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view.index,name="index"),
    path('daysentence/',daysentence_view.give_sentence),
    path('disanketang/',disanketang_index),
    path('qingganpin/',qingganpin_index),
    path('gongsi/',gongsi_index),
    path(r'members/<int:a>',member_intruduce),
    url(r'^media/(?P<path>.*)$',serve, {"document_root": MEDIA_ROOT}),
    path('activity/<int:a>',activity_intrudce),
    path('seeqinggan/<int:order>',seeqinggan),
    path('qingganpin/',include('qingganpin.urls')),
    path('tolisen-<int:order>.html/',tolisen),
    path('gongsi/',include('gongsi.urls')),
    path('gongzuoshi/',include('gongzuoshi.urls')),
    path('fankui/',include('fankui.urls'))

]
