from django.urls import path

from wishlist.views import wishlist_view, wishlist_json, wishlist_add_json, wishlist_del_json, wishlist_remove_view, \
    wishlist_now_view

#  TODO Импортируйте ваше представление

app_name = 'wishlist'

urlpatterns = [
    path('wishlist/', wishlist_view, name="wishlist_view"),
    path('wishlist/api/add/<str:id_product>', wishlist_add_json, name="wishlist_add_json"),
    path('wishlist/api/del/<str:id_product>', wishlist_del_json, name="wishlist_del_json"),
    path('wishlist/api/', wishlist_json, name="wishlist_json"),
    path('wishlist/remove/<str:id_product>', wishlist_remove_view, name="remove_now_wishlist"),
    path('wishlist/add/<str:id_product>', wishlist_now_view, name="add_now_wishlist")
]