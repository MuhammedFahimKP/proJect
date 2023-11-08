from django.shortcuts import render,redirect
from django.views import View,generic
from log.models import Addresses
from shop.models import Cart,CartItem
from checkouts.models import Payment,Order,OrderItems,payment_methods,order_status
from django.utils import timezone
import sweetify


class CheckoutView(View):

    def get(self,request):

        try:
            cart = Cart.objects.get(user=self.request.user)
        except:
            cart = None 

        cartItems = CartItem.objects.filter(cart=cart) if cart else None
        addresses = Addresses.objects.filter(user=self.request.user)
        total=0
        tax = float()
        grand_total = 0
        if cartItems:
            for cartItem in cartItems:
                total+=cartItem.total_price
                tax += (cartItem.product.price % 18) * cartItem.qauntity
            # print(cartItem.product.price % 18 * cartItem.qauntity)
            

        grand_total = total + tax    

            



        
        context = {

            'cartitems' : cartItems,
            'addresses' : addresses,
            'total':total,
            'tax':tax,
            'grand_total': grand_total
        }

        if cartItems:
            return render(self.request,"checkouts/orders.html",context)
        return redirect("/")
        
        
    
    def post(self,request):
        radioValue = request.POST.get('address',None)
        current_date = timezone.now()
        tax          = 0
        total      = 0
        cart       = Cart.objects.get(user=self.request.user)
        address    = Addresses.objects.get(id=radioValue) 
        cartitems   = CartItem.objects.filter(cart=cart)
        payment    = Payment()
        payment.user = self.request.user
        payment.method = payment_methods[0][0]
        payment.payed_at = None
        payment.save()
        order  = Order()
        order.grand_total=0.0
        order.payment = payment
        order.user =  self.request.user
        order.address = address
        order.created = current_date
        order.status = order_status[3][0]
        order.save()

        for item in cartitems:
            orditm = OrderItems()
            orditm.order = order
            orditm.product= item.product
            orditm.quantity = item.qauntity
            orditm.save()
            total+=orditm.total_price
            tax += (orditm.product.price % 18) * orditm.quantity

        cart.delete()
          

        grand_total = total+tax 
        order.grand_total = grand_total
        order.save() 
        sweetify.sweetalert(self.request,icon="success",text=f"order Done",title="Done",timer='3000',position='top-end',toast=True)
        return redirect(self.request.META.get('HTTP_REFERER'))
    




class OrderListView(View):

    def get(self,request):
        order = Order.objects.filter(user=self.request.user)
        context={
            'order':order    
        }
        return render(self.request,"log\orderview.html",context)



class OrderCancelView(View):

    def get(self,request,pk):

        ord = Order.objects.get(id=pk)
        ord.status = order_status[1][0]
        ord.save()
        sweetify.sweetalert(self.request,icon="success",text=f"order canceled",title="Order",timer='3000',position='top-end',toast=True)
        return redirect("orders")


class OrderItemsListView(View):


    def get(self,request,pk):

        try:
            ord = Order.objects.get(id=pk,user=request.user)
        except:
            ord = None

        orditems = OrderItems.objects.filter(order=ord) if ord else None

        items=0
        for item in orditems:

            items += item.quantity 




        context = {
            'orditems':orditems,
            'ord':ord,
            'items':items,
        }
        return render(request,'orders/orderitemsview.html',context)


