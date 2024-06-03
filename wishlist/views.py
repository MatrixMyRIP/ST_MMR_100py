from django.contrib.auth import get_user
from django.http import JsonResponse
from django.shortcuts import render

from logic.services import view_in_wishlist
from store.models import DATABASE


# Create your views here.
# def wishlist_view(request):
#     if request.method == "GET":
#         return render(request, "wishlist/wishlist.html")  # TODO прописать отображение избранного. Путь до HTML - wishlist/wishlist.html


def wishlist_view(request):
    if request.method == "GET":
        current_user = get_user(request).username
        data = view_in_wishlist(request)[current_user]  # TODO получить продукты из избранного для пользователя
        if request.GET.get('format') == 'JSON':
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})
        # TODO сформировать список словарей продуктов с их характеристиками
        products = []  # Список продуктов
        for product_id in data['products'].items():
            product = DATABASE.get(product_id)
            products.append(product)
        return render(request, 'wishlist/wishlist.html', context={"products": products})
