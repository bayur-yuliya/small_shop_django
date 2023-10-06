from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories/", views.categories, name="categories"),
    path("product/", views.list_by_products, name="products"),
    path("product/<int:num_product>", views.product, name="one_product"),
]
