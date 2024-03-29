from django.urls import path
from . import views

app_name = 'produto' # produto:algo

urlpatterns = [
    path('',views.ListProduct.as_view(),name='list'),
    path('<slug>',views.DetailProduct.as_view(),name='detail'),
    path('addtocart/',views.AddToCart.as_view(),name='addtocart'),
    path('removefromcart/',views.RemoveFromCart.as_view(),name='removefromcart'),
    path('cart/',views.Cart.as_view(),name='cart'),
    path('finish/',views.Finish.as_view(),name='finish'),
]
