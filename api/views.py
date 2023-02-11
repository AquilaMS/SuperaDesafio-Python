from django.http import HttpResponse, JsonResponse
from rest_framework import authentication, permissions
from django.contrib.auth.hashers import make_password
from .models import User, Cart, Transaction, Product
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.db.models import F, Sum
from .serilializers import ProductSerializer
from rest_framework.renderers import JSONRenderer
import json


class Signup(APIView):

    def post(self, request, format=None):
        try:
            password = make_password(request.data['password'])
            username = request.data['username']
            email = request.data['email']
        except:
            return JsonResponse({'error': 'Missing fields'})

        checkerEmail = User.objects.filter(email=email).first()
        checkerUsername = User.objects.filter(username=username).first()
        if (checkerEmail or checkerUsername):
            return JsonResponse({'error': 'Register failed. Check email/password.'})

        insert_user = User.objects.create(
            email=email, password=password, username=username)
        insert_user.save()
        token = Token.objects.create(user=insert_user)
        return HttpResponse()


class ProductToCart(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        body = json.loads(request.body)
        try:
            id_product = body['id_product']
        except:
            return JsonResponse({'error': 'Missing id_product'})
        user = request.user
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
            return update_total_price()

    def delete(self, request, format=None):
        body = json.loads(request.body)
        user = request.user
        try:
            id_product = body['id_product']
        except:
            return JsonResponse({'error': 'Missing id_product'})
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


class Checkout(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        body = json.loads(request.body)
        user = request.user
        userCart = Cart.objects.get(id_user=user)
        allUserProduct = userCart.products.all()
        newTransaction = Transaction(id_user=user)
        newTransaction.save()
        result = newTransaction.bought.add(*allUserProduct)

        userCart.delete()

        return HttpResponse()


class FilterByPrice(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, reques, format=None):
        productsByPrice = Product.objects.order_by('-price')
        productSerialized = ProductSerializer(productsByPrice, many=True)
        json = JSONRenderer().render(productSerialized.data)
        return HttpResponse(json.decode())


class FilterByScore(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, reques, format=None):
        productsByScore = Product.objects.order_by('-score')
        productSerialized = ProductSerializer(productsByScore, many=True)
        json = JSONRenderer().render(productSerialized.data)
        return HttpResponse(json.decode())


class FilterByName(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, reques, format=None):
        productsByName = Product.objects.order_by('name')
        productSerialized = ProductSerializer(productsByName, many=True)
        json = JSONRenderer().render(productSerialized.data)
        return HttpResponse(json.decode())
