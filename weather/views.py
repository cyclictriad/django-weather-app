import requests
from django.shortcuts import render
from django.conf import settings
from .forms import CityForm

def get_weather_data(city):
    api_key = settings.OPENWEATHERMAP_API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

def index(request):
    weather_data = None
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = get_weather_data(city)
    else:
        form = CityForm()

    return render(request, 'weather/index.html', {'form': form, 'weather_data': weather_data})