from django.contrib import admin

from .models import Order, OrderPosition

admin.site.register(Order)
admin.site.register(OrderPosition)
