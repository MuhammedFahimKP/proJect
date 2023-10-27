from django.shortcuts import render
from django.views import View
import sweetify


# Create your views here.

"""  custom  admin views """

class AdminView(View):

    def get(self,request):

        if request.user.is_authenticated:

            sweetify.sweetalert(request,icon="success",text=f"{request.user.email.split('@')[0]}",title="authenticated as",timer='3000',position='top-end',toast=True)

        return render(request,'manager/dashboard.html')
    



class AddproductView(View):

    def get(self,request):
        return render(
            request,
            "manager/addproduct.html"
        )    
    


class ProductView(View):

    def get(self,request):
        return render(
            request,
            "manager/productview.html"
        )    
    



