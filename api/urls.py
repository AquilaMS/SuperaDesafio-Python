from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup/', view=views.Signup.as_view()),
    path('get-token/', view=obtain_auth_token),
    path('cart/add/', views.AddProductToCart.as_view()),

]
