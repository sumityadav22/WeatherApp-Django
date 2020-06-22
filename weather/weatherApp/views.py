import requests
from django.shortcuts import redirect, render
from .forms import CityForm
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
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)

def addCity(request):
    form = CityForm(request.POST)
    if form.is_valid():
        # Duplicate city check
        new_city = form.cleaned_data['name']
        existing_city_count = City.objects.filter(name = new_city).count()
        if existing_city_count == 0:
            # City name validation
            response = requests.get(url.format(new_city)).json()
            if response['cod'] == 200:
                form.save()
    return redirect('home')