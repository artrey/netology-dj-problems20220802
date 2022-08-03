from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=40)


class Stock(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    products = models.ManyToManyField(Product, through='StockPosition',
                                      related_name='stocks')


class StockPosition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='positions')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE,
                              related_name='positions')
    price = models.IntegerField(validators=[MinValueValidator(1)])
    qty = models.PositiveIntegerField()


class StockPosition2(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='positions')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE,
                              related_name='positions')
    price = models.IntegerField(validators=[MinValueValidator(1)])
    qty = models.PositiveIntegerField()
