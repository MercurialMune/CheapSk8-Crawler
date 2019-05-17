import requests
import json
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from .models import *


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', locals())


@login_required(login_url='/accounts/login')
def home(request):
    current_user = request.user
    all_olx = OlxPhone.objects.all()
    all_pigia = PigiaPhone.objects.all()
    random_quotes = requests.get('http://quotes.rest/qod.json?category=funny')
    # result = json.load(random_quotes)
    # print(result)

    if 'olx' in request.GET and request.GET["olx"]:
        olx_query = request.GET.get("olx")
        olx_response = OlxPhone.objects.filter(name__icontains=olx_query)

    if 'pigia' in request.GET and request.GET["pigia"]:
        pigia_query = request.GET.get("pigia")
        pigia_response = PigiaPhone.objects.filter(name__icontains=pigia_query)

    return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login')
def logout_view(request):
    logout(request)
