from django.db import models
from django.utils.html import mark_safe  # 将字符串标记为安全进行输出
from markdown import markdown  # 导入 markdown 插件,将markdown格式转化为html



class qingganwen(models.Model):
    date=models.DateTimeField(auto_now =True)
    topic=models.CharField(max_length=30)
    content=models.FileField(upload_to='qingganwen/')
    
    def __str__(self):
        return self.topic

class lisening(models.Model):
    date=models.DateField(auto_now=False)
    topic=models.CharField(max_length=30)
    story=models.TextField(max_length=2000)
    content=models.FileField(upload_to='dayting/')
    def __str__(self):
        return self.topic

# Create your models here.
