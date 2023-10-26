from django.db import models
from django.urls import reverse
from log.models import MyUser
class Category(models.Model):
    

    """         
      Category  models slugfiled only for url routing  
  
    """

    cat_name = models.CharField(max_length=200,unique=True)
    cat_img  = models.ImageField(null=True, blank=True,upload_to="cat_img")
    slug     = models.SlugField(max_length=100,unique=True)

    def __str__(self) -> str:
        return f"{self.cat_name}"
    

    def get_url(self):
        return reverse('products_by_category',args=[self.slug])
    

   







   

    
    class Meta:
        verbose_name        = 'Category'
        verbose_name_plural = 'Categories' 






class Brand(models.Model):

    
    """
      Brand models slugfiled only for url routing  
     
    """

    brand_name = models.CharField(max_length=200,unique=True)
    brand_img  = models.ImageField(null=True, blank=True,upload_to="brand_img")
    slug       = models.SlugField(max_length=100,unique=True)    

   

    def __str__(self)->str:
        return f"{self.brand_name}"
    
    class Meta:
        verbose_name        = 'Brand'
        verbose_name_plural = 'Brands' 








class Product(models.Model):
     

     """
      product models slugfiled only for url routing  
     
     """

     name          = models.CharField(max_length=100,unique=True)
     slug          = models.SlugField(max_length=100,unique=True)
     img           = models.ImageField(null=True,blank=True,upload_to="prod_img")
     Brand         = models.ForeignKey(Brand,on_delete=models.CASCADE)
     Category      = models.ForeignKey(Category,on_delete=models.CASCADE)
     stocks        = models.IntegerField(default=0)
     is_available  = models.BooleanField(default=False)
     created_date  = models.DateTimeField(auto_now_add=True)
     modified_date = models.DateTimeField(auto_now=True)
     price         = models.PositiveIntegerField(default=0)
     discrption    = models.TextField(max_length=500,blank=True) 

    
     def __str__(self) -> str:
        return  f"{self.name}"
    

     class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'



# class CartItem(models.Model):
#       product = models.ForeignKey(Product,on_delete=models.CASCADE)
#       qauntity = models.PositiveIntegerField(default=0)

# class Cart(models.Model):
#       user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
#       cartitems = models.ForeignKey(CartItem,on_delete=models.CASCADE)

