from django.contrib import admin

from .models import ProductCatalog, Product

admin.site.register(ProductCatalog)
admin.site.register(Product)
