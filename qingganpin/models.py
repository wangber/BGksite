from django.db import models

class qingganwen(models.Model):
    date=models.DateTimeField(auto_now =True)
    content=models.FileField(upload_to='qingganwen/')

# Create your models here.
