from django.core.management.base import BaseCommand

from catalog.models import Product, ProductCatalog


class Command(BaseCommand):
    help = """the command generates a fake products"""

    def handle(self, *args, **options):
        Product.objects.create(
            name="Тушь",
            category=ProductCatalog.objects.get(name="Косметика"),
            price=22.00,
        )
        for el in range(1, 6):
            category_obj = ProductCatalog.objects.get(name="Косметика", id=el)
            Product.objects.create(name="Пудра", category=category_obj, price=125.00)
            Product.objects.create(name="Помада", category=category_obj, price=52.00)
            Product.objects.create(name="Тушь", category=category_obj, price=222.00)
        self.stdout.write(self.style.SUCCESS("Все прошло успешно!"))
