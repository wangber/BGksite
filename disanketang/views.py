# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse


def disanketang_index(request):
    # return HttpResponse(u"欢迎看见")
    return render(request,"disanketang.html")
    

# Create your views here.
