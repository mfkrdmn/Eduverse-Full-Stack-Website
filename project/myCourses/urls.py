from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.myCourses.as_view(), name="myCourses"),
    path('dashboard/', views.userDashboard, name="userDashboard"),

]
