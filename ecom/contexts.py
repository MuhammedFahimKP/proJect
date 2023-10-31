from shop.models import Cart,CartItem

def nav_notifications(request):
    if request.user.is_authenticated:
        try:
             cart = Cart.objects.get(user=request.user)
        except:
             cart = None     

       
        return {
        'cart_count':   CartItem.objects.filter(cart=cart).count() if cart else 0
        }
    return{
        'cart_count':0
    }