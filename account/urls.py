from django.contrib import admin
from django.urls import path
from account import views



urlpatterns = [
    path('register/', views.Register, name="register"),
    path('login/', views.Login, name="login"),
    path('logout/',views.Logout, name="logout"),
  
]
