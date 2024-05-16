from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib import messages
from .bot import send_message

def index(request):
    return render(request, "index.html")


def cart(request):
    return render(request, "cart.html")


def chackout(request):
    return render(request, "chackout.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # Вывод сообщения в терминал
        print(f"Received message from: {name} <{email}>")
        print(f"Message: {message}")
        
        send_message(f"Ism: {name}\nEmail: {email}\nText:{message}")

        # Здесь можно добавить дополнительную обработку сообщения, например, сохранение в базу данных или отправку по электронной почте

         # Отправляем подтверждение об успешном получении сообщения
        return render(request, 'contact.html')
        
    else:
        return render(request, "contact.html")  # Если метод запроса не POST, просто отобразим страницу контактов

def shopdetail(request):
    return render(request, "shop-detail.html")


def shop(request):
    return render(request, "shop.html")


def testimonial(request):
    return render(request, "testimonial.html")


def xatolik(request):
    return render(request, "xatolik.html")
