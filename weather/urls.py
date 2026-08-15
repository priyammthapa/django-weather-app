from django.urls import path
from .views import home, weather_api

urlpatterns = [
    path("", home, name="home"),
    path("api/weather/", weather_api, name="weather_api"),
]