from django.db import models


class Order(models.Model):
    id_order = models.IntegerField(verbose_name="Order id")
    is_closed = models.BooleanField(default=False, verbose_name="Is closed")
    name_user = models.CharField(max_length=100, verbose_name="Name", null=True)
    phone_user = models.CharField(max_length=100, verbose_name="Phone", null=True)
    address = models.CharField(max_length=100, verbose_name="Address", null=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return str(self.id_order)


class OrderPosition(models.Model):
    order = models.ForeignKey("cart.Orders", on_delete=models.DO_NOTHING)
    product = models.ForeignKey("catalog.Product", on_delete=models.DO_NOTHING)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Order position"
        verbose_name_plural = "Order positions"
        ordering = ["-count"]
