from django.urls import path
from .import views

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
]
