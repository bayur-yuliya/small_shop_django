from django.db import models


class ProductCatalog(models.Model):
    name = models.CharField(max_length=130)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey("ProductCatalog", on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=1500, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return str(self.name)
