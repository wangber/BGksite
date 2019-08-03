from django.shortcuts import render

# Create your views here.
def gongsi_index(request):
    return render(request,"gongsi.html")

def xingfukuaile(request):
    return render(request,"xingfukuaile.html")
