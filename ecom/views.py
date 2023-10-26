
from django.views import View
from django.shortcuts import render
from django.urls import reverse
from shop.models import Category
import sweetify



class Home(View):

    


    def get(self,request):
        
        
        context={
            'cat':Category.objects.all()
        }

        if request.user.is_authenticated:
            sweetify.sweetalert(request,icon="success",text=f"{request.user.email}",customclass='sw-wide',title="authenticated as",timer='3000',position='top-end',toast=True)

        return render(request,"home.html",context)
    


