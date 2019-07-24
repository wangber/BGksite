# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from . import duanju_get


def give_sentence(request):
    # return HttpResponse(u"欢迎看见")
    t=duanju_get.get("123")
    return render(request,"daysen.html",{"juzi":t})
    

# Create your views here.
