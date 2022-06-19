from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('product/<int:pk>/', views.product, name='product'),
    path('warehouses/', views.warehouses, name='warehouses'),
    path('warehouse/<int:pk>/', views.warehouse, name='warehouse'),
]