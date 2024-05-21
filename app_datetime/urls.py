from django.urls import path
from .views import datetime_view

urlpatterns = [
    path('datetime/', datetime_view),
]