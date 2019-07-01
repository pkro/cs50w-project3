from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="orders_index"),
    path("cart", views.cart, name="orders_cart"),
]
