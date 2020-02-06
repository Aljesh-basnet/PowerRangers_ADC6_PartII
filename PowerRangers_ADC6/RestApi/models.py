from django.db import models

# Create your models here.
class ranger(models.Model):
  cname=models.CharField(max_length=120)
  roomtype=models.CharField(max_length=120)
  cemail=models.EmailField()
