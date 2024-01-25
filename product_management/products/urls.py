# products/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name='product-list-create'),
    path('create/', product_create, name='product-create'),
    path('update/<int:pk>/', product_update, name='product-update'),
    path('delete/<int:pk>/', product_delete, name='product-delete'),
    path('api/products/', ProductListAPIView.as_view(), name='api-product-list'),
    path('api/products/<int:pk>/', ProductDetailAPIView.as_view(), name='api-product-detail'),
]