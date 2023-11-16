from django.shortcuts import render,redirect
from django.views import View
from shop.models import Product
from .models import Whishlist,WhishlistItems
import sweetify



class AddTOWhishlistlistView(View):

      def get(self,request,slug):
           if request.user.is_authenticated:
                try:
                        wl = Whishlist.objects.get(user=request.user)

                except:
                        wl = Whishlist.objects.create(user=request.user)
                        wl.save()

                product = Product.objects.get(slug=slug)        
                
                try:
                        wlitem = WhishlistItems.objects.get(product=product,whishlist=wl)

                except:
                        wlitem = WhishlistItems.objects.create(product=product,whishlist=wl)         
                        wlitem.save()
                
                return redirect(self.request.META.get('HTTP_REFERER'))
           

class WhishListListView(View):
       
       def get(self,request):
              
              try:
                    whishlist = Whishlist.objects.get(user=request.user)
              except:
                     whishlist = None

              whishlistitems = WhishlistItems.objects.filter(whishlist=whishlist) if whishlist else None 

              if whishlistitems:
                     context = {
                            'whishlistitems': whishlistitems,
                     }
                     return render(self.request,"whishlist\whishlist.html",context)     
                    
              return redirect(self.request.META.get('HTTP_REFERER'))    

           


