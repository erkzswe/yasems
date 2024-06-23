from rest_framework import serializers

from bills.models import Bill, Product, Payment


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price"]


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ["id", "amount", "payer", "payee", "bill", "is_paid"]


class BillSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username", read_only=True)
    products = ProductSerializer(many=True)
    payments = PaymentSerializer(many=True)

    class Meta:
        model = Bill
        fields = ["id", "description", "owner", "contributors", "products", "payments"]
