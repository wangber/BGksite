from django.db import models

class jianyi(models.Model):
    content=models.TextField(max_length=200,verbose_name="问题内容")
    ider=models.CharField(max_length=30,verbose_name="提出人")
    def __str__(self):
        return self.ider

    class Meta:
        verbose_name="反馈"
        verbose_name_plural="反馈"


# Create your models here.
