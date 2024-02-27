from django.db import models


class Order(models.Model):
    opened_at = models.DateTimeField(auto_now_add=True, verbose_name="Opened at")
    closed_at = models.DateTimeField(verbose_name="Closed at", blank=True, null=True)
    is_closed = models.BooleanField(default=False, verbose_name="Is closed")
    is_processed = models.BooleanField(default=True, verbose_name="Is processed")

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return str(self.id_order)


class OrderPosition(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey("catalog.Product", on_delete=models.DO_NOTHING)
    count = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Order position"
        verbose_name_plural = "Order positions"
        ordering = ["-count"]