from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class User(AbstractUser):
    id_user = models.UUIDField(primary_key=True, default=uuid4, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    id_product = models.UUIDField(primary_key=True, default=uuid4, null=False)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    score = models.FloatField()
    image = models.CharField(max_length=255)


class Cart(models.Model):
    id_cart = models.UUIDField(primary_key=True, default=uuid4, null=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField(default=0, null=True)
    products = models.ManyToManyField(Product, default=0)


class Transaction(models.Model):
    id_transaction = models.UUIDField(
        primary_key=True, default=uuid4, null=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    bought = models.ManyToManyField(Product, default=0)
