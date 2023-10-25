from django.urls import path
from . import views

urlpatterns=[
    path('',views.ShopView.as_view(),name="shop"),
    path('<slug:category_slug>',views.ShopView.as_view(),name="products_by_category"),
]