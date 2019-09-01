from django.db import models

class type(models.Model):
    tname=models.CharField(max_length=20,verbose_name="分类")
    def __str__(self):
        return self.tname
    class Meta:
        verbose_name="视频类别"
        verbose_name_plural="视频类别"

class video(models.Model):
    vname = models.CharField(max_length=30,verbose_name="视频名")
    vtype = models.ForeignKey(type,on_delete=models.DO_NOTHING,verbose_name="视频分类")
    vdis = models.TextField(max_length=2000,verbose_name="视频描述")
    video_img = models.FileField(upload_to="gongzuoshi/imgs/",verbose_name="上传一张视频的封面图片吧！",default='gongzuoshi/imgs/default.png')
    vblianjie = models.CharField(max_length=50,verbose_name="B站链接，如果没有，那就填写'暂无'吧")
    videocontent=models.FileField(upload_to="gongzuoshi/",verbose_name="上传视频")
    def __str__(self):
        return self.vname
    class Meta:
        verbose_name="视频"
        verbose_name_plural="视频"

class member(models.Model):
    mname = models.CharField(max_length=30,verbose_name="成员名字")
    job = models.CharField(max_length=30,verbose_name="成员职务")
    jianjie = models.TextField(max_length=200,verbose_name="成员简介")
    def __str__(self):
        return self.mname
    class Meta:
        verbose_name = "工作室成员"
        verbose_name_plural = "工作室成员们"

# Create your models here.
