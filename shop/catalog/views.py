from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "catalog/index.html")


def categories(request):
    return render(request, "catalog/categories.html")


def list_by_products(request):
    return HttpResponse("Страница где показаны товары из определенной категории")


def product(request, num_product):
    return HttpResponse(
        f"<h1>Страница с карточкой товара (разделение по коду товара?) </h1><br> Товар под номером {num_product}"
    )
