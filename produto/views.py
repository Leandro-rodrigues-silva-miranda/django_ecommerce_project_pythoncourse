from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from . import models

class ListProduct(ListView):
    model = models.Product
    template_name = 'produto/lista.html'
    context_object_name = 'products'

class DetailProduct(View):
    pass 

class AddToCart(View):
    pass 

class RemoveFromCart(View):
    pass 

class Cart(View):
    pass 

class Finish(View):
    pass 

