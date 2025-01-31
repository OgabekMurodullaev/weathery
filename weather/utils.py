import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
application = get_wsgi_application()

import requests
from weather.models import Weather

cities = [
  {"city": "Tashkent", "country": "Uzbekistan"},
  {"city": "Samarkand", "country": "Uzbekistan"},
  {"city": "Bukhara", "country": "Uzbekistan"},
  {"city": "Namangan", "country": "Uzbekistan"},
  {"city": "Fergana", "country": "Uzbekistan"},
  {"city": "Andijan", "country": "Uzbekistan"},
  {"city": "Nukus", "country": "Uzbekistan"},
  {"city": "Moscow", "country": "Russia"},
  {"city": "St. Petersburg", "country": "Russia"},
  {"city": "Novosibirsk", "country": "Russia"},
  {"city": "Irkutsk", "country": "Russia"},
  {"city": "Minsk", "country": "Belarus"},
  {"city": "Istanbul", "country": "Turkey"},
  {"city": "Dubai", "country": "United Arab Emirates"},
  {"city": "Almaty", "country": "Kazakhstan"},
  {"city": "Bishkek", "country": "Kyrgyzstan"},
  {"city": "Tbilisi", "country": "Georgia"},
  {"city": "Frankfurt", "country": "Germany"},
  {"city": "Beijing", "country": "China"},
  {"city": "Delhi", "country": "India"},
  {"city": "London", "country": "United Kingdom"},
  {"city": "Paris", "country": "France"},
  {"city": "New York", "country": "United States"}
]

API_KEY = "57b9b292765040189f153014253001"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather_for_city(city_name, country_name):
    params = {
        'key': API_KEY,
        'q': f"{city_name}, {country_name}",
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if 'current' in data:
        weather_data = data['current']
        return {
            'city_name': city_name,
            'country_name': country_name,
            'lat': data['location']['lat'],
            'lon': data['location']['lon'],
            'temperature': weather_data['temp_c'],
            'wind_speed': weather_data['wind_kph'],
            'cloud_cover': weather_data['cloud']
        }
    else:
        return None

def update_weather():
    for city in cities:
        weather_data = get_weather_for_city(city['city'], city['country'])
        if weather_data:
            Weather.objects.update_or_create(
                city_name=weather_data['city_name'],  # Yangi yoki mavjud shahar bo'yicha tekshiriladi
                country_name=weather_data['country_name'],
                defaults=weather_data  # Yangi ma'lumotlarni yangilash uchun
            )

update_weather()
