from django.db import models
class zhizhu(models.Model):
    name=models.CharField(max_length=30,verbose_name = "宠物名称")
    introduce=models.TextField(max_length=2000,verbose_name = "宠物简介")
    zhuimage=models.FileField(upload_to='zhizhuimage/',verbose_name = "上传一张最能代表它的图片吧")
    def __str__(self):
        return self.name
    class Meta:
     verbose_name_plural = '宠物'
     verbose_name = "宠物"
class gudong(models.Model):
    name=models.CharField(max_length=20,verbose_name = "股东名称")
    own=models.FloatField(verbose_name = "所占份额")
    joinday=models.DateField(auto_now=False,verbose_name = "加入日期")
    latestday=models.DateField(auto_now=True,verbose_name = "最近一次信息更新日期")
    class Meta:
     verbose_name_plural = "股东"
     verbose_name = "股东"
    def __str__(self):
         return self.name

# Create your models here.
