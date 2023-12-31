from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories/", views.categories, name="categories"),
    path("products_list/<int:categories_id>", views.list_by_products, name="products"),
    path("product/<int:num_product>", views.product, name="one_product"),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(), name="login"),
]
