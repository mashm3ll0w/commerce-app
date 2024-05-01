from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, CategorySerializer, ProductSerializer, OrderSerializer, CartSerializer, CartViewSerializer
from .permissions import IsAdmin
from .models import Category, Product, Order, User, Cart

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]
  def get_queryset(self):
    userId = self.request.user.id
    return User.objects.filter(pk=userId)

class RegisterViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  def get_queryset(self):
    return []
  
class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [IsAuthenticated]

class CartViewSet(viewsets.ModelViewSet):
  queryset = Cart.objects.all()
  serializer_class = CartSerializer
  permission_classes = [IsAuthenticated]
  def get_queryset(self):
    user = self.request.user
    return Cart.objects.filter(user=user)
  
class CartListView(viewsets.ModelViewSet):
  queryset = Cart.objects.all()
  serializer_class = CartViewSerializer
  permission_classes = [IsAuthenticated]
  def get_queryset(self):
    user = self.request.user
    return Cart.objects.filter(user=user)

class OrderViewSet(viewsets.ModelViewSet):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer
  permission_classes = [IsAuthenticated]
  def get_queryset(self):
    user = self.request.user
    return Order.objects.filter(cart__user=user)
