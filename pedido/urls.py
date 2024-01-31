from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('',views.DetailOrder.as_view(),name='detail'),
    path('pay/',views.PayOrder.as_view(),name='pay'),
    path('close/',views.CloseOrder.as_view(),name='close'),
]
