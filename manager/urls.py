from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.AdminView.as_view(),name="amdin"),
    path('addprd/',views.AddProductView.as_view(),name="addprd"),
    path('adminprd/',views.ProductView.as_view(),name="prd"),
    path('users/',views.AdminUserview.as_view(),name="users"),
    path('orders/',views.AdminOrderview.as_view(),name="admin-orders"),
    path('orders/order-item/<pk>',views.AdminOrderSigleView.as_view(),name="order-single-view")
    
]
