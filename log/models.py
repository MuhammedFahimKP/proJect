



from django.db import models
from django.utils import timezone

from .managers import MyUserManger
from django.utils.translation import gettext as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

# ?Create your models here.





class MyUser(AbstractBaseUser,PermissionsMixin):
   


    """
     django cutom user model class with permssion mixin

    """
   
    

    email          = models.EmailField(_('email_address'),unique=True)
    first_name     = models.CharField(max_length=150)
    last_name      = models.CharField(max_length=150)

    """
    required fields 

    """

    date_joined    = models.DateTimeField(default=timezone.now())
    last_login     = models.DateTimeField(default=timezone.now())
    is_staff       = models.BooleanField(default=False)
    is_superuser   = models.BooleanField(default=False)
    is_active      = models.BooleanField(default=True)

     
    objects = MyUserManger() 

    """
       we are teling that model required fields and 
       usernamefield      
    """ 

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
       return self.email.split('@')[0]
    

   

state_choices = [

      ("KR","Kerala"),
      ("KA","Karnataka"),
      ("TN","TamilNadu")
]





    # def __str__(self):
    #     return f"{self.user.first_name}  {self.state}" 
    
    



class Addresses(models.Model):


    """
    
    address model for the users

    
    """

    user            = models.ForeignKey(MyUser,on_delete= models.CASCADE,verbose_name="Customers")
    pin_code        = models.CharField(max_length=6,verbose_name="pincode" )
    city            = models.CharField(max_length=100)
    state           = models.CharField(choices=state_choices,max_length=50)
    place           = models.CharField(max_length=100)
    landmark        = models.CharField(max_length=100)
    phone_no        = models.CharField(max_length=10,verbose_name="phone no")
    alter_phone_no  = models.CharField(max_length=10,verbose_name="alternate phone no")


