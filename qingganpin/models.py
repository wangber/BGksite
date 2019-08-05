from django.db import models
from django.utils.html import mark_safe  # 将字符串标记为安全进行输出
from markdown import markdown  # 导入 markdown 插件,将markdown格式转化为html



class qingganwen(models.Model):
    date=models.DateTimeField(auto_now =True,verbose_name="最近更新日期")
    topic=models.CharField(max_length=30,verbose_name="主题")
    content=models.FileField(upload_to='qingganwen/',verbose_name="文章上传")
    
    def __str__(self):
        return self.topic
    class Meta:
     verbose_name_plural = '情感频文章'
     verbose_name = "情感频文章"

class lisening(models.Model):
    date=models.DateField(auto_now=False,verbose_name="发布日期")
    topic=models.CharField(max_length=30,verbose_name="发布主题")
    story=models.TextField(max_length=2000,verbose_name="写下你想分享的故事")
    content=models.FileField(upload_to='dayting/',verbose_name="上传你的歌曲吧")
    def __str__(self):
        return self.topic
    class Meta:
     verbose_name_plural = '每日一听歌曲录'
     verbose_name = "每日一听歌曲录"

# Create your models here.
