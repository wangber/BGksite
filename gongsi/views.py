from django.shortcuts import render
from .models import zhizhu,gudong
# Create your views here.
def gongsi_index(request):
    return render(request,"gongsi.html")

def xingfukuaile(request):
    gu=gudong.objects.order_by('-own')
    for i in gu:
        i.own = str(i.own*100)+"%"
    zhi=zhizhu.objects.order_by('-id')[:2]
    return render(request,"xingfukuaile.html",{'zhizhu':zhi,'gudong':gu})

def chongwuxiangqing(request,order):
    zhi=zhizhu.objects.get(id=order)
    return render(request,'chongwuxiangqing.html',{'zhizhu':zhi})
def allchongwu(request):
    zhi=zhizhu.objects.filter()
    return render(request,'allchongwu.html',{'zhizhu':zhi})
