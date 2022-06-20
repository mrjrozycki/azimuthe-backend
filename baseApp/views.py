from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


from .models import Product, Warehouse

from .serializers import ProductSerializer, WarehouseSerializer


class WarehouseList(APIView):
    def get(self, request):

        page = request.GET.get('page')
        # if pagination should work by default
        # page = request.GET.get('page', 1)
        per_page = 10

        warehouses = Warehouse.objects.all()

        if page:
            start = (int(page) - 1) * per_page
            end = start + per_page
            warehouses = warehouses[start:end]

        serializer = WarehouseSerializer(warehouses, many=True)
        return Response(serializer.data)


class ProductList(APIView):
    def get(self, request):
        f = request.GET.get('f')
        page = request.GET.get('page')
        # if pagination should work by default
        # page = request.GET.get('page', 1)
        per_page = 10

        if f:
            products = Product.objects.filter(warehouse=f)
        else:
            products = Product.objects.all()

        if page:
            start = (int(page) - 1) * per_page
            end = start + per_page
            products = products[start:end]

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK,
                        )


class ProductManage(APIView):  
    def post(self, request):
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        try:
            product = Product.objects.get(id=request.data["id"])
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
