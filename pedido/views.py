from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse


class PayOrder(View):

    def get(self,*args, **kwargs):
        return HttpResponse('Pagar')

class CloseOrder(View):

    def get(self,*args, **kwargs):
        return HttpResponse('Fechar pedido')

class DetailOrder(View):
    
    def get(self,*args, **kwargs):
        return HttpResponse('Detalhes')
