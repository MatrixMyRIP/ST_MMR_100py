from datetime import datetime

import requests
from django.http import JsonResponse

DIRECTION_TRANSFORM = {
    'n': 'северное',
    'nne': 'северо - северо - восточное',
    'ne': 'северо - восточное',
    'ene': 'восточно - северо - восточное',
    'e': 'восточное',
    'ese': 'восточно - юго - восточное',
    'se': 'юго - восточное',
    'sse': 'юго - юго - восточное',
    's': 'южное',
    'ssw': 'юго - юго - западное',
    'sw': 'юго - западное',
    'wsw': 'западно - юго - западное',
    'w': 'западное',
    'wnw': 'западно - северо - западное',
    'nw': 'северо - западное',
    'nnw': 'северо - северо - западное',
    'c': 'штиль',
}

def current_weather(request):
    if request.method == "GET":

        access_key = '52732ac9-6ac6-48b2-9aae-fa8eff8a1c26'
        url = f"https://api.weather.yandex.ru/v2/forecast?lat=59.93&lon=30.31"
        headers = {"X-Yandex-API-Key": f"{access_key}"}
        response = requests.get(url, headers=headers)
        data = response.json()
        result = {
            'city': data['geo_object']['locality']['name'],
            # Если используете Тариф «Погода на вашем сайте», то закомментируйте эту строку
            'time': datetime.fromtimestamp(data['fact']['uptime']).strftime("%H:%M"),
            # Если используете Тариф «Погода на вашем сайте», то закомментируйте эту строку
            'temp': data['fact']['temp'],  # TODO Реализовать вычисление температуры из данных полученных от API
            'feels_like_temp': data['fact']['feels_like'],
            # TODO Реализовать вычисление ощущаемой температуры из данных полученных от API
            'pressure': data['fact']['pressure_mm'],  # TODO Реализовать вычисление давления из данных полученных от API
            'humidity': data['fact']['humidity'],  # TODO Реализовать вычисление влажности из данных полученных от API
            'wind_speed': data['fact']['wind_speed'],
            # TODO Реализовать вычисление скорости ветра из данных полученных от API
            'wind_gust': data['fact']['wind_gust'],
            # TODO Реализовать вычисление скорости порывов ветка из данных полученных от API
            'wind_dir': DIRECTION_TRANSFORM.get(data['fact']['wind_dir']),
            # Если используете Тариф «Погода на вашем сайте», то закомментируйте эту строку
        }
        return JsonResponse(result, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})

# from lab_1_my.weather_api_my import current_weather
# def my_view(request):
#     if request.method == "GET":
#         data = current_weather(59.93, 30.31)  # Результат работы функции current_weather
#         # А возвращаем объект JSON. Параметр json_dumps_params используется, чтобы передать ensure_ascii=False
#         # как помните это необходимо для корректного отображения кириллицы
#         return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
#                                                      'indent': 4})

