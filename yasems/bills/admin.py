from django.contrib import admin
from bills.models import Product, Bill, Payment


admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Payment)
