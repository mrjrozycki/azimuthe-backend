from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.ProductList.as_view(), name='products'),
    path('product/', views.ProductManage.as_view(), name='product'),
    path('warehouses/', views.WarehouseList.as_view(), name='warehouses'),
]