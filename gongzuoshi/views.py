from django.shortcuts import render
from .models import member,type,video
def gongzuoshi_index(request):
    me=member.objects.filter()
    ty=type.objects.filter()
    vi=video.objects.filter()
    return render(request,'gongzuoshi.html',{'member':me,'type':ty,'video':vi})

def seevideo(request,order):
    vi=video.objects.get(id=order)
    return render(request,'seevideo-.html',{'video':vi})

def videotype(request,order):
    ty=type.objects.get(id=order)
    vi=video.objects.filter(vtype=ty)
    return render(request,'videotype.html',{'type':ty,'video':vi})



# Create your views here.
