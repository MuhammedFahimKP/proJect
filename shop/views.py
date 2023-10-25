from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Category,Product
# Create your views here.

class ShopView(View):

    def get(self,request,category_slug=None):
        if category_slug !=None:
                categories=get_object_or_404(Category,slug=category_slug)
                # product=Product.objects.all().filter(category=categories,is_available=True)
                # product_count = product.count()
        else:
                product=Product.objects.all().filter(is_available=True)
                # product_count = product.count()
                categories =Category.objects.all()
                

        context={
                'categories':categories,
                'product':product,
        }
        return render(
                request,
                'shop.html',
                context
        )