from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)  # This auto-generates a unique ID
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
