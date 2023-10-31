from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View,generic
from shop.models import Product
from .froms import ProductCreationForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from log.models import MyUser
from django.db.models import Q
import sweetify



# Create your views here.

"""  custom  admin views """

# @method_decorator(user_passes_test(lambda u:is_superuser))
class AdminView(View):

    def get(self,request):

        if request.user.is_authenticated:

            sweetify.sweetalert(request,icon="success",text=f"{request.user.email.split('@')[0]}",title="authenticated as",timer='3000',position='top-end',toast=True)

        return render(request,'manager/dashboard.html')
    






class AddProductView(generic.CreateView):

    form_class = ProductCreationForm  # Use your custom form class here
    model = Product  # Replace with your model
    template_name = 'manager/addproduct.html'
    success_url = reverse_lazy('addprd')

    def form_valid(self, form):
        sweetify.sweetalert(self.request,icon="success",text=f"Producte added",title="Done",timer='3000',position='top-end',toast=True)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        sweetify.sweetalert(self.request,icon="error",text=f"failed to add product",title="failed",timer='3000',position='top-end',toast=True)
        return super().form_invalid(form)
    
        


class ProductView(View):

    def get(self,request):
        prd = Product.objects.all() 
        context = {

            'products':prd,

        }
        
        return render(
            request,
            "manager/productview.html",
            context
        )    
    



class AdminUserview(View):

    def get(self,request):
        users = MyUser.objects.all()
        context = {'users':users}
        return render(request,"manager/users.html",context)


