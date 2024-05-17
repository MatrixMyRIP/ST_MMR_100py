from django.http import JsonResponse
from lab_1_my.weather_api_my import current_weather


def my_view(request):
    if request.method == "GET":
        data = current_weather(59.93, 30.31)  # Результат работы функции current_weather
        # А возвращаем объект JSON. Параметр json_dumps_params используется, чтобы передать ensure_ascii=False
        # как помните это необходимо для корректного отображения кириллицы
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})
