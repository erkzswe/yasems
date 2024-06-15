from django.db import models


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bill = models.ForeignKey('Bill', on_delete=models.SET_NULL, null=True)


class Bill(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey('core.Profile', on_delete=models.CASCADE)
    contributors = models.ManyToManyField('core.Profile', related_name="bills", blank=True)
    products = models.ManyToManyField('bills.Product', related_name="bills", blank=True)
