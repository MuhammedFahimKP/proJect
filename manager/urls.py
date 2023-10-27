from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.AdminView.as_view(),name="amdin"),
    path('addprd/',views.AddproductView.as_view(),name="addprd"),
    path('adminprd/',views.ProductView.as_view(),name="prd")
]