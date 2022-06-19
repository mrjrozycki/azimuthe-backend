from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, unique=True)
    stock = models.IntegerField()
    # I assume that if we delete the warehouse we dont want the products to just disappear
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.name



