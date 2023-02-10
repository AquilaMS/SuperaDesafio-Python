from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup/', view=views.Signup.as_view()),
    path('get-token/', view=obtain_auth_token),
    path('cart/', views.ProductToCart.as_view()),
    path('cart/checkout/', views.Checkout.as_view()),
    path('cart/filter/score/', views.FilterByScore.as_view()),
    path('cart/filter/name/', views.FilterByName.as_view()),
    path('cart/filter/price/', views.FilterByPrice.as_view()),
]
