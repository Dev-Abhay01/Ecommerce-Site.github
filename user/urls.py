from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home),
    path('about/',views.about),
    path('contactus/',views.contactus),
    path('services/',views.services),
    path('signin/',views.signin),
    path('signup/',views.register),
    path('createblog/',views.createblog),
    path('latestblog/',views.latestblog),
    path('myblogs/',views.myblog),
    path('myprofile/',views.myprofile),
    path('editprofile/',views.editprofile),
    path('logout/',views.logout),
]