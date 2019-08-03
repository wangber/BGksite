from django.db import models

# Create your models here.
class members(models.Model):
   mid=models.CharField(max_length=30)
   introduction=models.CharField(max_length=500)
   hobby=models.CharField(max_length=500)
   mimage=models.FileField(upload_to='memberimage/')
   def __str__(self):
       return self.mid
class happytime(models.Model):
   hid=models.CharField(max_length=30)
   title=models.CharField(max_length=30)
   text=models.CharField(max_length=2000)
   author=models.CharField(max_length=30)
   himage=models.FileField(upload_to='happyimage/')
   def __str__(self):
       return self.title
   def profile(self):
       if len(str(self.text))>=5:
           return "{}......".format(str(self.text))
       else:
           return str(self.text)
   profile.allow_tags=True

class activity(models.Model):
    topic=models.CharField(max_length=30)
    text=models.TextField(max_length=2000)
    holder=models.CharField(max_length=20)
    def __str__(self):
        return self.topic
    def profile(self):
       if len(str(self.text))>=5:
           return "{}......".format(str(self.text))
       else:
           return str(self.text)
    profile.allow_tags=True
