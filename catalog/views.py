import datetime
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def index(request):
    stuff = Product.objects.all()
    context = {'stuff': stuff}
    return render(request, 'stuff_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        with open('feedback.txt', 'a') as file:
            file.write(f'{timestamp}, {name},{phone}: {message}\n')

    return render(request, 'contacts.html')
