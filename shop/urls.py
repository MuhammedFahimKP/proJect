from django.urls import path
from . import views

urlpatterns=[
    path('',views.ShopView.as_view(),name="shop"),
    path('single/<str:slug>',views.SingleItemView.as_view(),name="shop-single"),
    path('<slug:category_slug>',views.ShopView.as_view(),name="products_by_category"),
    path('addcart/<slug:prd_slug>',views.AddToCart.as_view(),name="addtocart"),
    path('cart/',views.CartView.as_view(),name="cart"),
    path('increase/<pk>',views.IncreaseCart.as_view(),name="increase"),
    path('decrease/<pk>',views.DecreaseCart.as_view(),name="decrease"),
    path('delete_cartitem/<pk>',views.DeleteCart.as_view(),name="delete_cartitem"),
    # path('whishlist/',views.WhishListView.as_view(),name="whishlist")
]