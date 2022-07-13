from django.urls import path
from . import views

urlpatterns = [
    
    path('login', views.loginin, name="loginin"),
     path('register/', views.user_register, name="register"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.logout, name="logout"),

]
