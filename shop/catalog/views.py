from django.shortcuts import render, get_object_or_404

from catalog.forms import RegisterUserForm
from catalog.models import ProductCatalog, Product


def register(request):
    if request.method == "GET":
        form = RegisterUserForm()
        return render(request, "catalog/register.html", {"form": form})

    form = RegisterUserForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, "catalog/register.html", {"form": form})


def index(request):
    catalogs = ProductCatalog.objects.all()
    products = Product.objects.all()
    return render(
        request, "catalog/index.html", {"catalogs": catalogs, "products": products}
    )


def categories(request):
    catalogs = ProductCatalog.objects.all()
    return render(request, "catalog/categories.html", {"catalogs": catalogs})


def list_by_products(request, categories_id):
    catalogs = get_object_or_404(ProductCatalog, id=categories_id)
    products = Product.objects.filter(category=catalogs.id)

    return render(request, "catalog/list_by_products.html", {"products": products})


def product(request, num_product):
    products = Product.objects.get(id=num_product)
    return render(request, "catalog/product.html", {"products": products})
