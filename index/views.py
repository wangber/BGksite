from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    mem=members.objects.all()
    ha=happytime.objects.all()
    ac=activity.objects.all()
    return render(request,"index.html",{'memebers':mem,'happytime':ha,'activity':ac})

