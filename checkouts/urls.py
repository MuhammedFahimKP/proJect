from django.urls import path
from . import views

urlpatterns = [

    path('',views.OrderListView.as_view(),name="orders"),
    path('checkout/',views.CheckoutView.as_view(),name="checkout"),
    path('ordercancel/<int:pk>/',views.OrderCancelView.as_view(),name="order-cancel"),
    path('orderitems/<int:pk>/',views.OrderItemsListView.as_view(),name="order-items"),
]
