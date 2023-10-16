from django.http import HttpResponse
from django.shortcuts import render


def cart(request):
    return HttpResponse(
        "Страница корзины, где будет отображаться товары которые выбрали и подтверждение к формированию заказа"
    )


def create_order(request, num_order):
    return HttpResponse(
        f"Страница, где будет формироваться заказ {num_order} и загружаться в базу данных"
    )
