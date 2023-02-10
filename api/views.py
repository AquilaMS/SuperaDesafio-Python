from django.http import HttpResponse, JsonResponse
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


class ProductToCart(APIView):
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

        def update_total_price():
            item_count = Cart.objects.get(id_user=user).products.all().count()
            userCartSum = Cart.objects.annotate(
                price=Sum(F('products__price'))
            ).get(id_user=user)
            userCartSum.total_price = userCartSum.price
            userCartSum.save()

            frete = item_count * 10
            if userCartSum.total_price >= 250:
                frete = 0
            total_price = userCartSum.total_price + frete

            return JsonResponse({
                'subtotal': userCartSum.total_price,
                'frete': frete,
                'total': total_price
            })

        if (checkUseCart):
            checkUseCart.products.add(product)
            return update_total_price()
        else:
            userCart.save()
            userCart.products.add(product)
            update_total_price()
            return HttpResponse()

    def delete(self, request, format=None):
        body = json.loads(request.body)
        user = request.user
        id_product = body['id_product']
        product = Product.objects.get(id_product=id_product)
        checkUseCart = Cart.objects.filter(id_user=user).first()
        userCart = Cart(id_user=user)
        print(checkUseCart)

        def update_total_price():
            userCartSum = Cart.objects.annotate(
                price=Sum(F('products__price'))
            ).get(id_user=user)
            userCartSum.total_price = userCartSum.price
            userCartSum.save()

        if (checkUseCart):
            checkUseCart.products.remove(product)
            update_total_price()
            return HttpResponse()
        else:
            userCart.save()
            userCart.products.remove(product)
            update_total_price()
            return HttpResponse()
