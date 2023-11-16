from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.views import View,generic
from .models import MyUser,Addresses
from .forms import AddressCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .emailthread import EmailThread 
from django.http import HttpResponse
from django.conf import settings
from checkouts.models import order_status,Order

import sweetify



#creat your view
class SignupView(View):
  
    def get(self,request):
        
        if request.user.is_authenticated:
            return redirect('home')
         
        return render(request,'log/signup.html')

    def post(self,request):

        context={
            'error':None,
            'res':None
        }

        email = request.POST.get('email')
        if  MyUser.objects.filter(email=email).exists():
            context['error'] = 'you already have an accout'
        else:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            pass2 = request.POST.get('pass2')
            password = make_password(pass2)

            user  = MyUser.objects.create(email=email,first_name=fname,last_name=lname,password=password,is_active=False)
            user.save()
            EmailThread(email=email,req=request,user=user).start()
            sweetify.sweetalert(request,icon="success",text="To activate account",title="Check Mail",timer='5000')
            context['res'] = 'sucess account created activate your account using the link send to the mail'
        return render(request,'log/signup.html',context)
    
    



class Activation(View):

    def get(self,request,uidb64,token):

        try:
            uid = urlsafe_base64_decode(uidb64).decode()

            user = MyUser._default_manager.get(pk=uid)

        except(TypeError,ValueError,OverflowError,MyUser.DoesNotExist):
            user = None
        
        
        if user is not None and default_token_generator.check_token(user, token):
            
            user.is_active = True
            user.save()
            messages.success(request,'Your account is activated now you can login')
            return redirect('signin') 
        
        else:
            messages.error(request,'Your  Token is not valid ')
            return redirect('signin')
        
        return redirect('signin')
        

      





class SigninView(View):

    def get(self,request):

        if request.user.is_authenticated:
            return redirect('home')
        
        return render(request,'log/signin.html')
    
    def post(self,request):

        context = {

            'error':None
        }
        
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')

        user  = authenticate(email=email,password=pass1)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            context['error']="Wrong Password Or Email"         

        print(user)

        return render(request,'log/signin.html',context)
    


# class AccountView(View):

#     def get(self,reqeust):
#         return render(reqeust,'log/account.html')
    


class SignoutView(View):

    def get(self,request):
        logout(request)
        return redirect('home')


class AccountView(View):

    def get(self,request):
        return render(request,'log/account.html')

   


class AddressCreateView(generic.CreateView):

    form_class    = AddressCreationForm
    template_name = "addresscreate.html"
    success_url   = reverse_lazy('create-address')

    def form_valid(self, form):
        form.instance.user = self.request.user
        sweetify.sweetalert(self.request,icon="success",text=f"Address added",title="Done",timer='3000',position='top-end',toast=True)
        return super().form_valid(form)
    

    def form_invalid(self, form):
        sweetify.sweetalert(self.request,icon="error",text=f"Give a proper Address ",title="Failed",timer='3000',position='top-end',toast=True)
        return super().form_invalid(form)
    



class AddressView(generic.ListView):
    model               = Addresses 
    template_name       = "addressview.html"
    context_object_name = 'objects'


    def get_queryset(self): 
        return Addresses.objects.filter(user=self.request.user)


class AddressDeleteView(generic.DeleteView):

    model         = Addresses
    success_url   = reverse_lazy('address')
    template_name = "add_delete_conf .html"
    # items_to_delete = []

    def delete(self,*args, **kwargs):

        try:
            address = self.get_object()
            address.delete()
            sweetify.sweetalert(self.request,icon="success",text=f"Address Deleted",title="Done",timer='3000',position='top-end',toast=True)
        except :
            sweetify.sweetalert(self.request,icon="success",text=f"there is no address",title="failed",timer='3000',position='top-end',toast=True)

        super().delete(self.request,*args,**kwargs)      



    

