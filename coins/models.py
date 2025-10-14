from decimal import Decimal

from django.db import models


class Coin(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    price = models.DecimalField(
        max_digits=20,
        decimal_places=8,
        default=Decimal('0.0'),
    )
    rank = models.IntegerField(default=0, blank=True)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['rank']
