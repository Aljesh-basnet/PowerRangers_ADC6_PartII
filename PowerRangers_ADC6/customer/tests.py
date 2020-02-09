from django.test import TestCase
from .models import BookRoom,Room,Hotels
from django.contrib.auth.models import User

class ModelTestCase(TestCase):       
        def setUp(self):
            hostel = Hotels.objects.create(Name="Your Dream Hotel")
            location = Hotels.objects.create(Location="Chitwan")


        def test_book_name(self):
        book1=BookRoom.objects.get(name="Aljesh")
        self.assertEqual(books.name,"Aljesh")
    
        def test_valid_phone(self):
        book2=BookRoom.objects.get(phone="9866313335")
        value=book2.is_valid_phone()
        self.assertFalse(value,True)

        def test_valid_bookroom(self):
        b = BookRoom.objects.get(arrival="2016-02-25",checkOut="2018-03-25")
        value=b.is_valid_book()
        self.assertTrue(b,True)

        def test_description(self):
        description = Hotels.objects.get(Description = 'Welcome to Our Hotel')
        self.assertEqual(description.Description, 'Welcome to Our Hotel') 