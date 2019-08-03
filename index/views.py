from django.shortcuts import render,HttpResponse
from .models import *


# Create your views here.
def index(request):
    mem=members.objects.all()
    ha=happytime.objects.all()
    ac=activity.objects.all()
    
    return render(request,"index.html",{'memebers':mem,'happytime':ha,'activity':ac})

def member_intruduce(request,a):
    mem=members.objects.get(id=a)
    content={'mem':mem}
    return render(request,"member.html",content)

def activity_intrudce(request,a):
    ac=activity.objects.get(id=a)
    content={'ac':ac}
    return render(request,"activity.html",content)
    

