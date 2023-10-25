



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
    

   




