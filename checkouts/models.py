from django.db import models
from log.models import MyUser,Addresses
from shop.models import Product
from datetime import timedelta
# Create your models here.


payment_methods=[

           ("Cash On Delivery","Cash On Delivery"),

]

order_status = [
            ("Delivered","Delivered"),
            ("Canceled","Canceled"),
            ("Pending","Pending"),
            ('Shipping','Shipping'),
]



class Payment(models.Model):
      user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
      method = models.CharField(choices=payment_methods,max_length=50,null=True,default=None)
      amount_payed = models.DecimalField(default=0.0,decimal_places=2,max_digits=15)
      payed_at = models.DateTimeField(null=True,blank=True)

      @property
      def is_payed(self)->bool:
            return True if self.payed_at  else False
 


      class Meta:
            ordering = ['payed_at']






class Order(models.Model):
    

      user    = models.ForeignKey(MyUser,on_delete=models.CASCADE)
      address = models.ForeignKey(Addresses,on_delete=models.CASCADE)
      created = models.DateTimeField(editable=True,auto_now_add=True)
      status  = models.CharField(choices=order_status,max_length=50,default=None,null=True)
      grand_total = models.DecimalField(default=0.0,decimal_places=2,max_digits=15)
      payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
      
      @property
      def order_id(self)-> str:
            return str(self.pk) + str(self.created)
      

      @property
      def expected(self)-> str:
            return str(self.created.date() + timedelta(days=7))  
      
      def __str__(self)-> str:
            return self.order_id      

      class Meta:
            ordering = ['-created']

class OrderItems(models.Model):
      order = models.ForeignKey(Order,on_delete=models.CASCADE)
      product = models.ForeignKey(Product,on_delete=models.CASCADE)
      quantity = models.PositiveIntegerField(default=0)


      @property
      def total_price(self) ->int:
            return self.product.price * self.quantity

      def __str__(self)->str:
            return f"{self.order.order_id}"
      class Meta:
            ordering = ['quantity']




      