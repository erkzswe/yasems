from django.contrib.auth.models import User
from rest_framework import generics
from core.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def root(request, format=None):
    return Response(
        {
            "users": reverse("users-list", request=request, format=format),
            "bills": reverse("bills-list", request=request, format=format),
            "products": reverse("products-list", request=request, format=format),
        }
    )


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
