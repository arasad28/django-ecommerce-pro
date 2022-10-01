from distutils.command.upload import upload
from hashlib import blake2b
from tabnanny import verbose
from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Categories'

def upload_file(instance,filename):
    return instance.created.strftime("products/%Y%m%d") + instance.post.id
class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='author')
    image = models.ImageField(upload_to='products')
    title = models.CharField(max_length=264)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    short_description = models.TextField(max_length=200)
    full_description = models.TextField()
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    q_deal = models.BooleanField(default=False)
    q_deal_req = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created']
    
    def discount(self):
        if self.old_price>self.price:
            return int(((self.old_price-self.price)/self.old_price)*100)
        else:
            return False
class Slider(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='slider_product')
    image = models.ImageField(upload_to='products/slider',help_text="please add image 750*416 px for slider",blank=True,null=True)
    slide = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product.title} slider:{self.slide}'