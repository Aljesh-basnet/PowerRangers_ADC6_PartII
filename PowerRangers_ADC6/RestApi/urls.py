from django.urls import path
from RestApi.views import *
urlpatterns=[
    path('APK',rangerDetail),
    path('APK/<int:Id>',rangerUpDe),
    path('APK/<int:PageNo>/<int:items>',pagination)
]