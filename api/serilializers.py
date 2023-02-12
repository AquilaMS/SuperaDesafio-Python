from rest_framework import serializers
from .models import Product, Transaction


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class TransactionSerilializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
