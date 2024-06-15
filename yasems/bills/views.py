from django.http import Http404, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from bills.models import Product, Bill
from bills.serializers import BillSerializer, ProductSerializer


class ProductView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk=pk)
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    def delete(self, request, pk):  
        product = self.get_object(pk=pk)
        product.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        print(type(serializer))
        print(dir(serializer))
        print(type(serializer.data))
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


class BillView(APIView):
    def get_object(self, pk):
        try:
            return Bill.objects.get(pk=pk)
        except Bill.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk=pk)
        serializer = BillSerializer(product)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk=pk)
        serializer = BillSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    def delete(self, request, pk):  
        product = self.get_object(pk=pk)
        product.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)


class BillListView(APIView):
    def get(self, request):
        products = Bill.objects.all()
        serializer = BillSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)