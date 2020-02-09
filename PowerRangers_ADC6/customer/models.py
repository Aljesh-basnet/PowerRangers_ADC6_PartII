from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

class BookRoom(models.Model):
    cname = models.CharField(max_length=20)
    roomtype =models.CharField(max_length=20)
    roomno=models.IntegerField()
    cemail = models.EmailField()
    phone=models.IntegerField()
    arrival=models.DateField()
    checkOut=models.DateField()
    cfile =models.URLField()
    
    def __str__(self):
        return f"{self.cname} has booked {self.roomno}"
    
    def is_valid_phone(self):
        return self.phone >=0

    def is_valid_bookroom(self):
        return self.arrival != self.checkOut


class Hotel_Image(models.Model):
    hotel_image = models.URLField()
    hotel_name = models.CharField(max_length=50)
    hotel_description = models.CharField(max_length=70)


# Stores all the hotel details and is used to query hotels.
class Hotels(models.Model):
    Name = models.CharField(max_length  = 255)
    Address = models.CharField(max_length  = 255)
    City = models.CharField(max_length  = 255)
    Country = models.CharField(max_length  = 255)
    TelephoneNumber = models.CharField(max_length=12)
    ImagePath = models.CharField(max_length  = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    Description = models.TextField(max_length  = 140)
    class Meta:
        verbose_name_plural = 'Hotels'

    def get_absolute_url(self):
        return reverse('hoteldetails', kwargs={'pk': self.pk})
    def __str__(self):
         return self.Name

# Stores the Hotels rooms
class Room(models.Model):
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    RoomType = models.CharField(max_length  = 255)
    Capacity = models.IntegerField(default = 0)
    BedOption = models.CharField(max_length  = 255)
    Price= models.IntegerField(default = 0)
    View = models.CharField(max_length  = 255)
    TotalRooms = models.CharField(max_length  = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Room'

    def __str__(self):
         return self.RoomType





