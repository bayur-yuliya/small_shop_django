from django.urls import path

from . import views

urlpatterns = [
    path("", views.cart, name="cart"),
    path("order/<int:num_order>", views.create_order, name="order"),
]
