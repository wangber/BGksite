from django.shortcuts import render,HttpResponse
from .models import *


# Create your views here.
def index(request):
    mem=members.objects.all()
    ha=happytime.objects.filter().order_by('-id')[:5]
    ac=activity.objects.all()
    
    return render(request,"index.html",{'memebers':mem,'happytime':ha,'activity':ac})

def member_intruduce(request,a):
    mem=members.objects.get(id=a) #找到人
    lold = mem.lol_date
    #将胜率转成百分数
    lold.win_of_all = str(lold.win_of_all*100)+"%"
    lold.win_of_pipei = str(lold.win_of_pipei*100)+"%"
    lold.win_of_paiweil = str(lold.win_of_pipei*100)+"%"

    content={'mem':mem,'lol':lold}
    return render(request,"member.html",content)

def activity_intrudce(request,a):
    ac=activity.objects.get(id=a)
    content={'ac':ac}
    return render(request,"activity.html",content)
    

