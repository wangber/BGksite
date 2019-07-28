from django.db import models

# Create your models here.
class members(models.Model):
   mid=models.CharField(max_length=30)
   introduction=models.CharField(max_length=500)
   hobby=models.CharField(max_length=500)
   def __str__(self):
       return self.mid
class happytime(models.Model):
   hid=models.IntegerField()
   title=models.CharField(max_length=30)
   text=models.CharField(max_length=2000)
   author=models.CharField(max_length=30)
   def __str__(self):
       return self.hid
class activity(models.Model):
    topic=models.CharField(max_length=30)
    text=models.TextField(max_length=2000)
    holder=models.CharField(max_length=20)
    def __str__(self):
        return self.topic
