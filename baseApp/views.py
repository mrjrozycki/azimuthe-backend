from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Warehouse

from .serializers import ProductSerializer, WarehouseSerializer


def home(request):
    return HttpResponse("Home page")

@api_view(['GET'])
def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT'])
def product(request, pk):
    if request.method == 'GET':
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        data = request.data
        data['warehouse'] = pk
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        try:
            product = Product.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return HttpResponse(status=404)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def warehouses(request):
    if request.method == 'GET':
        warehouses = Warehouse.objects.all()
        serializer = WarehouseSerializer(warehouses, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'POST', 'PUT'])
def warehouse(request, pk):
    if request.method == 'GET':
        try:
            warehouse = Warehouse.objects.get(pk=pk)
            serializer = WarehouseSerializer(warehouse)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WarehouseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        try:
            warehouse = Warehouse.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Warehouse does not exist'}, status=404)
        serializer = WarehouseSerializer(warehouse, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

