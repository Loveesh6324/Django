from django.urls import path
from .views import cart
from User import views

urlpatterns = [
    path('cart/', cart.as_view(), name='cart'),
    path('checkout/', views.checkout),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
]
