from django.db import models
from log.models import MyUser
from shop.models import Product

# Create your models here.


class Whishlist(models.Model):

    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)




class WhishlistItems(models.Model):

    whishlist = models.ForeignKey(Whishlist,on_delete=models.CASCADE)
    product   = models.ForeignKey(Product,on_delete=models.CASCADE)
    


