from django.db import models
from django.conf import settings
from django.conf import *

class BookRoom(models.Model):
    cname = models.CharField(max_length=20)
    roomtype =models.CharField(max_length=20)
    roomno=models.IntegerField()
    cemail = models.EmailField()
    ccontact = models.CharField(max_length=15)
    cfile =models.URLField()
    
    def __str__(self):
        return f"{self.cname} has booked {self.roomno}"



class Destination(models.Model):
    destination_image = models.URLField()
    destination_name = models.CharField(max_length=50)
    destination_description = models.CharField(max_length=70)