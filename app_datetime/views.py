from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from datetime import datetime



def datetime_view(request):
    if request.method == "GET":
        data = datetime.now()
        # return HttpResponse(data)
        return HttpResponse(data.strftime('%H:%M %d/%m/%y'))


# Create your views here.

