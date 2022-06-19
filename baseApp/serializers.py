from rest_framework import serializers
from .models import Product, Warehouse

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ('id', 'name', 'city', 'street', 'zipcode', 'country')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'stock', 'warehouse', 'created', 'updated')
