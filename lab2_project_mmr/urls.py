"""
URL configuration for lab2_project_mmr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import random

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

from app_datetime.views import datetime_view
from app_weather.views import my_view
from store.views import shop_view, products_view


def random_view(request):
    if request.method == "GET":
        data = round(random.uniform(1, 100), 4)
        return HttpResponse(data)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('random/', random_view),
    path('', include('store.urls')),
    path('', include('app_datetime.urls')),
    path('', include('app_weather.urls')),
    path('', include('app_login.urls')),
    path('', include('wishlist.urls'))

]

