from django.urls import path
from .import views
from checkouts import views as Ord

urlpatterns = [

    path('signup/',views.SignupView.as_view(),name="signup"),
    path('activate/<uidb64>/<token>',views.Activation.as_view(),name='activate'),
    path('signin/',views.SigninView.as_view(),name='signin'),
    path('account/',views.AccountView.as_view(),name='Account'),
    path(
        'signout',
        views.SignoutView.as_view(),
        name='Signout'
    ),
    path('account/',views.AccountView.as_view(),name="accounts"),
    path('address/create',views.AddressCreateView.as_view(),name="create-address"),
    path('address/',views.AddressView.as_view(),name="address"),
    path('deleteaddress/<int:pk>',views.AddressDeleteView.as_view(),name="delete-address"),
   
]
