from django.db import models


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Bill(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey('core.User')
    contributors = models.ManyToManyField('core.User', related_name='contributors', blank=True)
    