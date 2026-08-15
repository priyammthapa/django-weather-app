import requests
from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, 'weather/index.html')


def weather_api(request):
    city = request.GET.get('city')

    if not city:
        return JsonResponse({'error': 'Please enter a city'}, status=400)

    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_params = {
        'name': city,
        'count': 1,
        'language': 'en',
        'format': 'json'
    }

    geo_response = requests.get(geo_url, params=geo_params)
    geo_data = geo_response.json()

    if 'results' not in geo_data:
        return JsonResponse({'error': 'City not found'}, status=404)

    location = geo_data['results'][0]

    latitude = location['latitude']
    longitude = location['longitude']

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        'latitude': latitude,
        'longitude': longitude,
        'current': 'temperature_2m,relative_humidity_2m,weather_code',
        'timezone': 'auto'
    }

    weather_response = requests.get(weather_url, params=weather_params)
    weather_data = weather_response.json()

    return JsonResponse({
        'city': location['name'],
        'country': location.get('country'),
        'temperature': weather_data['current']['temperature_2m'],
        'humidity': weather_data['current']['relative_humidity_2m'],
        'weather_code': weather_data['current']['weather_code']
    })