import datetime
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView, CreateView
from catalog.models import Product
from django.urls import reverse_lazy
from .models import BlogPost


# def index(request):
#     stuff = Product.objects.all()
#     context = {'stuff': stuff}
#     return render(request, 'stuff_list.html', context)


class IndexView(ListView):
    model = Product
    template_name = 'stuff_list.html'
    context_object_name = 'stuff'


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'product_detail.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#         with open('feedback.txt', 'a') as file:
#             file.write(f'{timestamp}, {name},{phone}: {message}\n')
#
#     return render(request, 'contacts.html')

class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        with open('feedback.txt', 'a') as file:
            file.write(f'{timestamp}, {name},{phone}: {message}\n')
        return super().get(request, *args, **kwargs)

