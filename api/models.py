from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Category(models.Model):
    name=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)#change at the time of object creation
    updated_at=models.DateTimeField(auto_now=True)#change each time

    def __str__(self):
        return self.name
    
class Product(models.Model):
    title=models.CharField(max_length=200)   
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="items")
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=200,null=True)
    picture=models.ImageField(upload_to="images",default="default.jpg",null=True)
    is_trending=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Basket(models.Model):
    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="cart")
    is_active=models.BooleanField(default=True)  
    created_at=models.DateTimeField(auto_now_add=True)  
    updated_at=models.DateTimeField(auto_now=True)
    @property
    def cart_items(self):
        #qs=Baskitem.objects.filter(basket=self)
        qs=self.cartitem.all()
        return qs


class BasketItem(models.Model):
    basket=models.ForeignKey(Basket,on_delete=models.CASCADE,related_name="cartitem")   
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    is_active=models.BooleanField(default=True)  
    created_at=models.DateTimeField(auto_now_add=True)  
    updated_at=models.DateTimeField(auto_now=True)
    total=models.PositiveIntegerField(null=True,blank=True)

    def save(self,*args,**kwargs):
        if not self.total:
            self.total=self.product.price*self.quantity
        super().save(*args,**kwargs)    


    def create_basket(sender,instance,created,**kwargs) :
        if created:
            Basket.objects.create(owner=instance)
    post_save.connect(create_basket,sender=User)



    


