from django.shortcuts import render
from django.http import HttpResponse
from .models import jianyi
def fankui_index(request):
    return render(request,"fankui.html")
def fankui_store(request):
    jianyicontent = request.POST["jianyi"]
    jianyiren = request.POST["ider"]
    if jianyicontent != '' and jianyiren != '':
        try:

            jianyi.objects.get_or_create(content=jianyicontent, ider=jianyiren)
            return HttpResponse("建议提交成功"+"<br><a href=\"/\">返回首页</a>"+"<br>")
        except:
            return HttpResponse("建议提交失败，你是不是和别人提交了一样的建议呢？换一个试试吧"+"<br><a href=\"/\">返回首页</a>"+"<br>"+"<a href='#' onClick='javascript :history.go(-1);'>返回上一页</a>")
    else:
        return HttpResponse("建议提交失败，你是不是提交了空的建议呢？换一个试试吧"+"<br><a href=\"/\">返回首页</a>"+"<br>"+"<a href='#' onClick='javascript :history.go(-1);'>返回上一页</a>")




# Create your views here.
