from django.db import models

# Create your models here.
class members(models.Model):
   mid=models.CharField(max_length=30,verbose_name="成员ID")
   introduction=models.TextField(max_length=500,verbose_name="成员简介")
   hobby=models.CharField(max_length=500,verbose_name="成员爱好")
   mimage=models.FileField(upload_to='memberimage/',verbose_name="上传一张最具代表性的图片吧")
   def __str__(self):
       return self.mid
   class Meta:
     verbose_name_plural = "成员"
     verbose_name = "成员"
class happytime(models.Model):
   hid=models.CharField(max_length=30,verbose_name="时光代号")
   title=models.CharField(max_length=30,verbose_name="时光主题")
   text=models.CharField(max_length=2000,verbose_name="时光内容")
   author=models.CharField(max_length=30,verbose_name="作者")
   himage=models.FileField(upload_to='happyimage/',verbose_name="上传一张最具代表性的图片吧")
   def __str__(self):
       return self.title
   class Meta:
     verbose_name_plural = '开心时光'
     verbose_name = "开心时光"

class activity(models.Model):
    topic=models.CharField(max_length=30,verbose_name="活动主题")
    text=models.TextField(max_length=2000,verbose_name="活动内容")
    holder=models.CharField(max_length=20,verbose_name="主持人")
    def __str__(self):
        return self.topic
    class Meta:
     verbose_name_plural = '经典活动'
     verbose_name = "经典活动"
