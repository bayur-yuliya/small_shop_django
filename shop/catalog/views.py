from django.shortcuts import render, get_object_or_404

from cart.models import Order, OrderPosition
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
    catalog = get_object_or_404(ProductCatalog, id=categories_id)
    products = Product.objects.filter(category=catalog.id)

    return render(
        request,
        "catalog/list_by_products.html",
        {"products": products, "catalog": catalog},
    )


def product(request, num_product):
    products = get_object_or_404(Product, id=num_product)
    if request.method == "POST":
        order, created = Order.objects.get_or_create(id=1)
        order_position, created = OrderPosition.objects.get_or_create(
            order=order, product=products
        )
        if created is True:
            order_position.count = 1
        elif created is False and order.is_processed:
            OrderPosition.objects.filter(order=order, product=products).update(
                count=order_position.count + 1
            )

    return render(request, "catalog/product.html", {"products": products})
