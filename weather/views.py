from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def home(request):
    return render(request, "weather/index.html")

@api_view(['GET'])
def weather_api(request):
    return Response({
        "city": "Kolkata",
        "temperature": 30,
        "condition": "Cloudy"
    })