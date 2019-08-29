from django.db import models
# Create your models here.

class Loldata(models.Model):
    own_data = models.CharField(max_length=30,verbose_name="你的ID")
    num_of_all = models.IntegerField(verbose_name="总局数")
    win_of_all = models.FloatField(verbose_name="总胜率（将胜率装换为小数输入哦，比如50%则输入0.5）")
    num_of_pipei = models.IntegerField(verbose_name="匹配场数")
    win_of_pipei = models.FloatField(verbose_name="匹配胜率（将胜率装换为小数输入哦，比如50%则输入0.5）")
    num_of_paiwei = models.IntegerField(verbose_name="排位场数")
    win_of_paiwei = models.FloatField(verbose_name="排位胜率（将胜率装换为小数输入哦，比如50%则输入0.5）")
    hero_often = models.TextField(max_length=1000,verbose_name="常用英雄,如果是多个英雄用/分隔开",default="无")
    location_often = models.TextField(max_length=100,verbose_name="常打位置,如果是多个位置用/分隔开",default="无")
    now_level = models.CharField(max_length=50,verbose_name="目前段位",default="无")
    max_level = models.CharField(max_length=50,verbose_name="最高段位",default="无")
    date_latest= models.DateTimeField(verbose_name='数据更新时间',auto_now=True)
    def __str__(self):
       return self.own_data
    class Meta:
     verbose_name_plural = "成员LOL数据"
     verbose_name = "成员LOL数据"

class members(models.Model):
   mname = models.CharField(max_length=30,verbose_name="成员姓名")
   mid=models.CharField(max_length=30,verbose_name="成员ID")
   skills = models.TextField(max_length=300,verbose_name="说一说技能特长吧")
   one_sen = models.TextField(max_length=100,verbose_name="书写一句最能展示自己个性的话吧")
   mimage=models.FileField(upload_to='memberimage/',verbose_name="上传一张最具代表性的图片吧")
   hobby=models.CharField(max_length=500,verbose_name="成员爱好")
   BGk_dis = models.TextField(max_length=1000,verbose_name="书写一下自己在BGk的角色自我描述吧")
   introduction=models.TextField(max_length=500,verbose_name="在这尽情书写你的简介")
   lol_date = models.ForeignKey(Loldata,verbose_name='你的LOL数据',on_delete=models.CASCADE)
   
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
