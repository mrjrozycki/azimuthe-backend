from django.db import models

class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    warehouse = models.CharField(max_length=255)

    def __str__(self):
        return self.name