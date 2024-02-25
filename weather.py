import requests
from cache import WeatherCache
from secret import API_KEY

weather_cache = WeatherCache()
API_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + API_KEY


def fetch_weather(city):
    """Получение погоды по названию города. Добавлен кэш. Возвращает градусы по цельсию."""
    cached_data = weather_cache.get(city)
    if cached_data:
        return cached_data


    response = requests.get(API_URL.format(city))

    data = response.json()

    assert data['cod'] == 200

    temp_k = data['main']['temp']
    temp_c = round(temp_k - 273.15)

    weather_cache.set(city, temp_c)

    return temp_c

