import time


class WeatherCache:
    def __init__(self):
        self.cache = {}
        self.cache_duration = 600

    def get(self, city):
        """Получение данных из кэша, если они актуальны."""
        current_time = time.time()
        if city in self.cache and current_time - self.cache[city]['timestamp'] < self.cache_duration:
            return self.cache[city]['data']
        else:
            return None

    def set(self, city, data):
        """Добавление или обновление данных в кэше."""
        self.cache[city] = {
            'data': data,
            'timestamp': time.time()
        }