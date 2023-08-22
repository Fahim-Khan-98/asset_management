from django.urls import path
from asset_app import views



urlpatterns = [
    path('', views.home, name="home"),

]

