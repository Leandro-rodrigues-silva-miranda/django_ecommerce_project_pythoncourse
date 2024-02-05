from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from . import models

class ListProduct(ListView):
    model = models.Product
    template_name = 'produto/lista.html'
    context_object_name = 'products'
    paginate_by = 3

class DetailProduct(DetailView):
    model = models.Product
    template_name = 'produto/detalhe.html'
    context_object_name = 'products'
    slug_url_kwarg = 'slug'


class AddToCart(View):
    pass 

class RemoveFromCart(View):
    pass 

class Cart(View):
    pass 

class Finish(View):
    pass 

