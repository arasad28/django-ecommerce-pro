from django import views
from django.urls import path
from app_order import views

app_name = 'app_order'
urlpatterns = [
    path('cart/',views.cart_view,name='cart'),
    path('add/<pk>/',views.add_to_cart,name='add'),
    path('remove/<pk>/',views.remove_from_cart,name='remove'),
    path('increase/<pk>/',views.increment_cart,name='increase'),
    path('decrease/<pk>/',views.decrement_cart,name='decrease'),
]
