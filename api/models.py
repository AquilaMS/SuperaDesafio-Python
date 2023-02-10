from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class User(AbstractUser):
    id_user = models.UUIDField(primary_key=True, default=uuid4, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    id_product = models.UUIDField(primary_key=True, default=uuid4, null=False)
    price = models.FloatField()
    score = models.FloatField()
    image_ref = models.CharField(max_length=255)


class Cart(models.Model):
    id_cart = models.UUIDField(primary_key=True, default=uuid4, null=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField()
    products = models.ManyToManyField(Product)


class Transaction(models.Model):
    id_transaction = models.UUIDField(
        primary_key=True, default=uuid4, null=False)
