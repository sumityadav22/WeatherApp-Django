import requests
from django.shortcuts import render
from .models import City

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0661a8746b03f7d4cb59ceecde0ff3f6'

def index(request):
    city = "Mumbai"
    response = requests.get(url.format(city)).json()
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        city_weather = {
                'city': city.name.capitalize(),
                'temperature': response['main']['temp'],
                'description': response['weather'][0]['description'].capitalize(),
                'icon': response['weather'][0]['icon']
            }
        weather_data.append(city_weather)
    context = {'weather_data': weather_data}
    return render(request, 'weather/weather.html', context)
