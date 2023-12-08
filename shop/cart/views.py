from django.shortcuts import render


def create_order(request, num_order):
    return render(request, "cart/create_order.html")


def cart(request):

    return render(request, "cart/cart.html")
