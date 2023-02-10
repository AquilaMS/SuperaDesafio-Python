from django.http import HttpResponse
from rest_framework import authentication, permissions
from django.contrib.auth.hashers import make_password
from .models import User, Cart, Transaction, Product
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.db.models import F, Sum
import json


class Signup(APIView):

    def post(self, request, format=None):
        password = make_password(request.data['password'])
        username = request.data['username']
        email = request.data['email']
        checkerEmail = User.objects.filter(email=email).first()

        checkerEmail = User.objects.filter(email=email).first()
        checkerUsername = User.objects.filter(username=username).first()
        if (checkerEmail):
            return HttpResponse({'error': 'Register failed. Check email/password.'})
        if (checkerUsername):
            return HttpResponse({'error': 'Register failed. Check email/password.'})

        insert_user = User.objects.create(
            email=email, password=password, username=username)
        insert_user.save()
        token = Token.objects.create(user=insert_user)
        return HttpResponse(insert_user)


class AddProductToCart(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        body = json.loads(request.body)
        user = request.user
        id_product = body['id_product']
        product = Product.objects.get(id_product=id_product)
        checkUseCart = Cart.objects.filter(id_user=user).first()
        userCart = Cart(id_user=user)
        print(checkUseCart)
        if (checkUseCart):
            itemsCount = Cart.objects.get(id_user=user).products.all().count()
            userCartSum = Cart.objects.annotate(
                price=Sum(F('products__price')*itemsCount)
            ).get(id_user=user)
            userCartSum.total_price = userCartSum.price
            userCartSum.save()
            return HttpResponse(userCartSum.total_price)
        else:
            userCart.save()
            userCart.products.add(product)
