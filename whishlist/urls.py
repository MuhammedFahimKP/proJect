from django.urls import path
from  . import views
urlpatterns = [
    path('addtowhishlist/<str:slug>',views.AddTOWhishlistlistView.as_view(),name="add_to_whishlist"),
    path('',views.WhishListListView.as_view(),name="whishlist"),
]
