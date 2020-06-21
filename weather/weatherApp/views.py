import requests
from django.shortcuts import render

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0661a8746b03f7d4cb59ceecde0ff3f6'

def index(request):
    city = "Mumbai"
    response = requests.get(url.format(city)).json()
    city_weather = {
            'city': city.name.capitalize(),
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'].capitalize(),
            'icon': response['weather'][0]['icon']
        }
    context = {'city_weather': city_weather}
    return render(request, 'weather/weather.html', context)
