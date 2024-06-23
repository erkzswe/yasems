from django.contrib.auth.models import User
from rest_framework import serializers
from bills.models import Bill
from core.models import Profile


class UserSerializer(serializers.ModelSerializer):
    # bills = serializers.PrimaryKeyRelatedField(many=True, queryset=Bill.objects.all())
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "profile",
        ]
