import requests
from django.shortcuts import render
from .models import *


def home(request):
    current_user = request.user
    all_olx = OlxPhone.objects.all()
    all_pigia = PigiaPhone.objects.all()
    random_quotes = requests.get('http://quotes.rest/qod.json?category=funny')

    if 'olx' in request.GET and request.GET["olx"]:
        olx_query = request.GET.get("olx")
        olx_response = OlxPhone.objects.filter(name__icontains=olx_query)

    if 'pigia' in request.GET and request.GET["pigia"]:
        pigia_query = request.GET.get("pigia")
        pigia_response = PigiaPhone.objects.filter(name__icontains=pigia_query)

    return render(request, 'index.html', locals())



