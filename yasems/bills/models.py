from django.db import models


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bill = models.ForeignKey("Bill", on_delete=models.SET_NULL, null=True)


class Bill(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey("core.Profile", on_delete=models.CASCADE)
    contributors = models.ManyToManyField(
        "core.Profile", related_name="bills", blank=True
    )
    products = models.ManyToManyField("bills.Product", related_name="bills", blank=True)
    sum = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class Payment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bill = models.ForeignKey("Bill", on_delete=models.CASCADE, related_name="payments")
    payer = models.ForeignKey("core.Profile", on_delete=models.SET_NULL, null=True)
    payee = models.IntegerField(
        blank=True, null=True
    )  # user id of person who we pay back, None if we've paid for that bill
    is_paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.payee:
            self.is_paid = True
        if self.amount > self.bill.sum:
            raise ValueError("Payment amount cannot be greater than bill amount")
        super().save(*args, **kwargs)
