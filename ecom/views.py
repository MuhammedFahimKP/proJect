from typing import Any
from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse
from log.models import MyUser
from django.contrib.auth import login
from django.conf import settings
from django.contrib import  messages
from shop.models import Category
import requests



class Home(generic.TemplateView):
    
    template_name = "home.html"
    


    def get_context_data(self, *args,**kwargs) -> dict[str, Any]:
        
        context = super(Home, self).get_context_data(*args,**kwargs)
        context['cat'] = Category.objects.all()

        return context
    


# def Home(request):
#     return render(request,'base.html')