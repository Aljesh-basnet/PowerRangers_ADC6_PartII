from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.index, name="index"),
    path('booking/',views.view_Booking_lists),
    path('bookingform/',views.booking_form, name="Bookingform"),
    path('bookingform/save',views.booking_save),
    path('booking/update/<int:ID>',views.booking_update_forms),
    path('booking/update/update/<int:ID>',views.booking_update_save),
    path('booking/delete/<int:ID>', views.delete_book),
    path('search/',views.search),
    path('search/searchlist',views.searchresults),
    path('uploadview/',views.upload_view,name="upload_view"),
    path('upload/upload/',views.upload_hotel,name="uploadimage"),
    path('signup/',views.register_user,name="signup"),
    path('login/',views.authenticate_user, name="login"),
    path('logout/',views.logout, name="logout")
    
   
]