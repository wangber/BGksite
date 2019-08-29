# coding:utf-8
from django.shortcuts import render
from .models import qingganwen,lisening
from django.shortcuts import render
from django.http import HttpResponse
from daysentence import duanju_get
from django.core.paginator import Paginator

def give_sentence(request):
    # return HttpResponse(u"欢迎看见")
    t=duanju_get.get("123")
    return render(request,"daysen.html",{"juzi":t})

def qingganpin_index(request):
    t=duanju_get.get("123")
    wen=qingganwen.objects.order_by('-id')[:3]#只显示id最大的3条
    music=lisening.objects.order_by('-id')[:3]
    con = {'wen':wen,'juzi':t,'music':music}
    return render(request,"qingganpin.html",con)

def seeqinggan(request,order):
    wen=qingganwen.objects.get(id=order)
    content={'date':wen.date,'con':wen.content,'topic':wen.topic}
    return render(request,"seeqingganwen.html",content)

def tolisen(request,order):
    song=lisening.objects.get(id=order)
    song_name = str(song.content).split('/')
    con = {'music':song.content,'song':song,'song_name':song_name[1]}
    return render(request,"tolisen-.html",context=con)

def seeallmusic(request):
   #构造分页器
    page_num = request.GET.get('page',1)
    allmu=lisening.objects.filter()
    music_afterpage = Paginator(allmu,5)
    need_page = music_afterpage.get_page(page_num)
    need_musics = need_page.object_list
    page_range = music_afterpage.page_range
    return render(request,"allmusic.html",{'music':need_musics,'page_range':page_range})

def seeallarticle(request):
   #构建分页器
    allar=qingganwen.objects.filter()
    page_num = request.GET.get('page',1) #获得前端的页码需求
    article_afterpage = Paginator(allar,5)#把所有文章分页
    need_page = article_afterpage.get_page(page_num)#从分页的文章中获得所需要的页
    articles_need = need_page.object_list #获得该页里面的所有文章对象
    page_range = article_afterpage.page_range
    con = {'wen':articles_need,'page_range':page_range,'need_page':need_page}
    return render(request,"seeallarticle.html",context=con)



# 彩蛋
def qixi(you):
 if (you.lovingstatus=="single"):
    return "试试就试试"
 else:
    return "谢谢参与"

# Create your views here.
