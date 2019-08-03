# coding:utf-8
from django.shortcuts import render
from .models import qingganwen,lisening
from django.shortcuts import render
from django.http import HttpResponse
from daysentence import duanju_get


def give_sentence(request):
    # return HttpResponse(u"欢迎看见")
    t=duanju_get.get("123")
    return render(request,"daysen.html",{"juzi":t})

def qingganpin_index(request):
    t=duanju_get.get("123")
    wen=qingganwen.objects.order_by('-id')[:3]#只显示id最大的3条
    music=lisening.objects.order_by('-id')[:3]
    return render(request,"qingganpin.html",{'wen':wen,'juzi':t,'music':music})

def seeqinggan(request,order):
    wen=qingganwen.objects.get(id=order)
    
    with open('media/'+str(wen.content),'r',encoding='utf-8') as f: a= f.read()
    content={'date':wen.date,'con':a}
    return render(request,"seeqingganwen.html",content)

def tolisen(request,order):
    song=lisening.objects.get(id=order)
    return render(request,"tolisen-.html",{'music':song.content,'song':song})

def seeallmusic(request):
    allmu=lisening.objects.filter()
    return render(request,"allmusic.html",{'music':allmu})

def seeallarticle(request):
    allar=qingganwen.objects.filter()
    return render(request,"seeallarticle.html",{'wen':allar})

def qixi(you):
 if (you.lovingstatus=="single"):
    return "试试就试试"
 else:
    return "谢谢参与"

# Create your views here.
