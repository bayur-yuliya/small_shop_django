from django.shortcuts import render


def index(request):
    return render(request, "catalog/index.html")


def categories(request):
    return render(request, "catalog/categories.html")


def list_by_products(request):
    return render(request, "catalog/list_by_products.html")


def product(request, num_product):
    return render(request, "catalog/product.html")
