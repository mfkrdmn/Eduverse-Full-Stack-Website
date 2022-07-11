from urllib import request
from django.urls import path
from . import views
from app.views import *
urlpatterns = [
    #path('', views.index, name="index"),
    path('', IndexView.as_view(), name="index"),
    #path('about', views.about, name="about"),
    path('about', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),

]
