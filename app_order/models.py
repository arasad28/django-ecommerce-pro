from django.db import models
from django.conf import settings

# import product model 
from app_shop.models import Product
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='cart')
    item = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product')
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quantity} X {self.item}'

    def get_total(self):
        total = self.item.price * self.quantity
        float_total = format(total,'0.2f')
        return float_total
    
class Order(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='order')
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=264,blank=True,null=True)
    orderId = models.CharField(max_length=264,blank=True,null=True)


    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        return total

class Comment(models.Model):
    prod = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_comment")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='comment_user')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date',)

    def __str__(self):
        return self.comment
