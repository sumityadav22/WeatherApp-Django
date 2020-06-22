import math
import requests
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import CityForm
from .models import City

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0661a8746b03f7d4cb59ceecde0ff3f6'

def index(request):
    form = CityForm()
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        response = requests.get(url.format(city)).json()
        fahrenheit_temperature = response['main']['temp']
        celsius_temperature = (fahrenheit_temperature - 32)*5 / 9
        city_weather = {
                'city': city.name.capitalize(),
                'temperature': math.ceil(celsius_temperature),
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
                messages.add_message(request,messages.SUCCESS,"City is added successfully !")
            else:
                messages.add_message(request, messages.WARNING,"Sorry we couldn't find the city you entered !")
        else:
            messages.add_message(request, messages.INFO,"City is already present in the database")
    return redirect('home')

def deleteCity(request):
    city = City.objects.all()
    city.delete()
    return redirect('home')

def about(request):
    return render(request, 'weather/about.html')