import requests
from datetime import datetime
import json

# Словарь перевода значений направления ветра
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


def current_weather(lat, lon):
    """
    Описание функции, входных и выходных переменных
    """
    # token = 'Ваш токен'  # Вставить ваш токен
    # url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}"  # Если вдруг используете тариф «Погода на вашем сайте»
    # # то вместо forecast используйте informers. url = f"https://api.weather.yandex.ru/v2/informers?lat={lat}&lon={lon}"
    # headers = {"X-Yandex-API-Key": f"{token}"}
    # response = requests.get(url, headers=headers)
    # data = response.json()

    access_key = 'dc2db323-e9cb-492f-a6e8-1747fc9b8a1f'
    url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}"
    headers = {"X-Yandex-API-Key": f"{access_key}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    # print(json.dumps(data, indent=4, ensure_ascii=False))
    # pass



    # Данная реализация приведена для тарифа «Тестовый», если у вас Тариф «Погода на вашем сайте», то закомментируйте пару строк указанных ниже
    # result = {
    #     'city': data['geo_object']['locality']['name'],  # Если используете Тариф «Погода на вашем сайте», то закомментируйте эту строку
    #     'time': datetime.fromtimestamp(data['fact']['uptime']).strftime("%H:%M"),  # Если используете Тариф «Погода на вашем сайте», то закомментируйте эту строку
    #     'temp': data['fact']['temp'],  # TODO Реализовать вычисление температуры из данных полученных от API
    #     'feels_like_temp': data['fact']['feels_like'],  # TODO Реализовать вычисление ощущаемой температуры из данных полученных от API
    #     'pressure': data['fact']['pressure_mm'],  # TODO Реализовать вычисление давления из данных полученных от API
    #     'humidity': data['fact']['humidity'],  # TODO Реализовать вычисление влажности из данных полученных от API
    #     'wind_speed': data['fact']['wind_speed'],  # TODO Реализовать вычисление скорости ветра из данных полученных от API
    #     'wind_gust': data['fact']['wind_gust'],  # TODO Реализовать вычисление скорости порывов ветка из данных полученных от API
    #     'wind_dir': DIRECTION_TRANSFORM.get(data['fact']['wind_dir']),  # Если используете Тариф «Погода на вашем сайте», то закомментируйте эту строку
    # }
    # return result
    s = f"Город: {data['geo_object']['locality']['name']}\n" \
        f"Время: {datetime.fromtimestamp(data['fact']['uptime']).strftime("%H:%M")}\n" \
        f"Температура: {data['fact']['temp']} градусов Цельсия\n" \
        f"Чувствуется как: {data['fact']['feels_like']} градусов Цельсия\n" \
        f"Давление: {data['fact']['feels_like']} мм. рт. ст.\n" \
        f"Влажность: {data['fact']['feels_like']} %\n" \
        f"Скорость ветра: {data['fact']['feels_like']} м/с\n" \
        f"Порывы ветра: {data['fact']['feels_like']} м/с\n" \
        f"Направление ветра: {DIRECTION_TRANSFORM.get(data['fact']['wind_dir'])}\n"

    return s

if __name__ == "__main__":
    print(current_weather(59.93, 30.31))  # Проверка работы для координат Санкт-Петербурга
