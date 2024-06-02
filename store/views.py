import json

from django.shortcuts import render

from django.http import JsonResponse, HttpResponseNotFound

from logic.services import filtering_category, view_in_cart, add_to_cart, remove_from_cart
from store.models import DATABASE
from django.http import HttpResponse


def products_view(request):
    if request.method == "GET":
        id_product = request.GET.get('id')
        if id_product:
            if id_product in DATABASE:
                return JsonResponse(data=DATABASE.get(id_product), json_dumps_params={'ensure_ascii': False, 'indent': 4})
            return HttpResponseNotFound("Данного продукта нет в базе данных")
        category_key = request.GET.get("category")  # Считали 'category'
        ordering_key = request.GET.get("ordering") # Если в параметрах есть 'ordering'
        if ordering_key:
            if request.GET.get("reverse") and request.GET.get("reverse").lower() == 'true': # Если в параметрах есть 'ordering' и 'reverse'=True
                data = filtering_category(DATABASE, category_key, ordering_key, True) #  TODO Использовать filtering_category и провести фильтрацию с параметрами category, ordering, reverse=True
            else:  # Если не обнаружили в адресно строке ...&reverse=true, значит reverse=False
                data = filtering_category(DATABASE, category_key, ordering_key) #  TODO Использовать filtering_category и провести фильтрацию с параметрами category, ordering, reverse=False
        else:
            data = filtering_category(DATABASE, category_key) #  TODO Использовать filtering_category и провести фильтрацию с параметрами category
        # В этот раз добавляем параметр safe=False, для корректного отображения списка в JSON
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False,
                                                                 'indent': 4})

# def shop_view(request):
#     if request.method == "GET":
#         with open('store/shop.html', encoding="utf-8") as f:
#             data = f.read()  # Читаем HTML файл
#         return HttpResponse(data)

from django.shortcuts import render

def shop_view(request):
    if request.method == "GET":
        return render(request, 'store/shop.html', context={"products": DATABASE.values()})


def products_page_view(request, page):
    if request.method == "GET":
        if isinstance(page, str):
            for data in DATABASE.values():
                if data['html'] == page:  # Если значение переданного параметра совпадает именем html файла
                    with open(f'store/products/{data['html']}.html', 'r', encoding="utf-8") as f:
                        return HttpResponse(f.read())
        elif isinstance(page, int):
            if str(page) in DATABASE:
                with open(f'store/products/{DATABASE[str(page)]['html']}.html', 'r', encoding="utf-8") as f:
                    return HttpResponse(f.read())
        # TODO 1. Откройте файл open(f'store/products/{page}.html', encoding="utf-8") (Не забываем про контекстный менеджер with)
        # TODO 2. Прочитайте его содержимое
        # TODO 3. Верните HttpResponse c содержимым html файла

        # Если за всё время поиска не было совпадений, то значит по данному имени нет соответствующей
        # страницы товара и можно вернуть ответ с ошибкой HttpResponse(status=404)
        return HttpResponse(status=404)

# def cart_view(request):
#     if request.method == "GET":
#         data = view_in_cart()  # TODO Вызвать ответственную за это действие функцию
#         return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
#                                                      'indent': 4})

def cart_view(request):
    if request.method == "GET":
        data = view_in_cart()
        json_param = request.GET.get("json")
        if request.GET.get('format') == 'JSON':
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})
        products = []  # Список продуктов
        for product_id, quantity in data['products'].items():
            product = DATABASE.get(product_id)
            product["quantity"] = quantity
            product["price_total"] = f"{quantity * product['price_after']:.2f}"  # добавление общей цены позиции с ограничением в 2 знака
            # 3. добавьте product в список products
            products.append(product)

        return render(request, "store/cart.html", context={"products": products})


def cart_add_view(request, id_product):
    if request.method == "GET":
        result = add_to_cart(id_product)  # TODO Вызвать ответственную за это действие функцию и передать необходимые параметры
        if result:
            return JsonResponse({"answer": "Продукт успешно добавлен в корзину"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное добавление в корзину"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})


def cart_del_view(request, id_product):
    if request.method == "GET":
        result = remove_from_cart(id_product)  # TODO Вызвать ответственную за это действие функцию и передать необходимые параметры
        if result:
            return JsonResponse({"answer": "Продукт успешно удалён из корзины"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное удаление из корзины"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})