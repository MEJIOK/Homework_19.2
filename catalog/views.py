from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Сохранение данных в базу данных
        Contact.objects.create(name=name, phone=phone, message=message)

        return HttpResponse('Thank you for your message!')

    return render(request, 'contacts.html')
