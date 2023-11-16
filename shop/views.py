from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from checkouts.models import Order,OrderItems
from .models import( 
      Category,
      Product,
      Cart,
      CartItem,
      Review
)

from .forms import ProductReviewForm
import sweetify
# Create your views here.

class ShopView(View):

    def get(self,request,category_slug=None):
        if category_slug !=None:
                categories=get_object_or_404(Category,slug=category_slug)
                product=Product.objects.all().filter(Category=categories,is_available=True)
                product_count = product.count()

                cat =  Category.objects.all()
        else:
                product=Product.objects.all().filter(is_available=True)
                product_count = product.count()
                cat  =Category.objects.all()
                
        context={
                'categories':cat ,
                'product':product,
                'productcount':product_count,
        }
        
        return render(
                request,
                'shop.html',
                context
        )
    


class SingleItemView(View):
      
      def get(self,request,slug):
            
            form = ProductReviewForm()

            try:
                  ord = Order.objects.filter(user=self.request.user)
                 
            except:
                  ord = None      


            k=False      


            try: 
                  product = Product.objects.get(slug=slug)
            except:
                  product = None

            if product:

                  if ord:

                        for order in ord:
                             
                          if OrderItems.objects.filter(order=order,product=product).exists():
                                k=True
                                break
                  
                  review = Review.objects.filter(product=product)
                  context = {
                        'product':product,
                        'reviews':review,
                        'form': form,
                        'isOrdered':k
                  }
                  return render(self.request,'shop/singleitem.html',context)
            else:
                  return redirect(self.request.META.get('HTTP_REFERER')) 
        
      def post(self,request,slug):
            
            form = ProductReviewForm(self.request.POST)
            product = Product.objects.get(slug=slug)
            
            if form.is_valid:
                  
                  form.instance.user = self.request.user
                  form.instance.product = product
                  form.save()
                  sweetify.sweetalert(request,icon="success",text=f"review added",title="Success",timer='3000',position='bottom-end',toast=True)
                  return redirect(self.request.META.get('HTTP_REFERER')) 

                
                  
                  

                                 
            
             

# def shopsingle(request):
#       return render(request,'shop/singleitem.html')             

class AddToCart(View):

      def get(self,request,prd_slug):
           if request.user.is_authenticated:
                try:
                        cart = Cart.objects.get(user=request.user)

                except:
                        cart = Cart.objects.create(user=request.user)
                        cart.save()

                product = Product.objects.get(slug=prd_slug)        
                
                try:
                        cartitem = CartItem.objects.get(product=product,cart=cart)
                        cartitem.qauntity=cartitem.qauntity+1         
                        cartitem.save()
                except:
                        cartitem = CartItem.objects.create(product=product,cart=cart,qauntity=1)         
                        cartitem.save()        

           return  redirect("shop")  
      


class CartView(View):
      
        def get(self,request):
            if request.user.is_authenticated:
                  try:
                        cart = Cart.objects.get(user=request.user)
                        
                  except:
                        cart = None

                  cartitems = CartItem.objects.filter(cart=cart) if cart else None      
                  cart_count = cartitems.count() if cartitems else 0

     
                  total = 0
                  items = 0
                  if  cart_count == 0 or  not cart:
                        return render(request,"emptycart.html")
                  
                  else:
                        for item in cartitems:
                              total += item.total_price
                              items += item.qauntity 
                              
                  
                  context={
                        'cartitem':cartitems,
                        'cart_count':cart_count,
                        'total':total if total else None,
                        'items':items if items else None,
                   }
                  return render(request,"cart.html",context)
            else:
                return redirect("/")                  
            


class IncreaseCart(View):
      
        def get(self,request,pk):
            cartitem = CartItem.objects.get(id=pk)
            cartitem.qauntity = cartitem.qauntity + 1
            cartitem.save() 
            return redirect("cart")
        

            



           
      


class DecreaseCart(View):

        def get(self,request,pk):
            cartitem = CartItem.objects.get(id=pk)
            if  cartitem.qauntity > 1:
                  cartitem.qauntity = cartitem.qauntity -1
                  cartitem.save()
                  
            else:
                sweetify.sweetalert(request,icon="error",text=f"quantity must be 1",title="failed",timer='3000',position='top-end',toast=True)     
            return redirect('cart')               
      

class DeleteCart(View):

        def get(slef,request,pk):
            cartitem = CartItem.objects.get(id=pk)
            cartitem.delete()
            sweetify.sweetalert(request,icon="success",text=f"product removed from cart",title="Success",timer='3000',position='top-end',toast=True)
            return redirect('cart')      
        


# class WhishListView(View):
      
#       def get(self,requst):
#             return render(self.request,'cart.html')
            
              