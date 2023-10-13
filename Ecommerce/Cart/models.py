from django.db import models
from Shop.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateField(auto_now_add=True)

    def subtotal(self):
        return self.quantity*self.product.price



class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    noofitems=models.IntegerField()
    place=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    order_status=models.CharField(max_length=20,default="pending")
    delivery_status=models.CharField(max_length=30,default="pending")
    date_added=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def subtotal(self):
        return self.noofitems * self.product.price


class Account(models.Model):
    AccountNumber=models.IntegerField()
    AccountType=models.CharField(max_length=200)
    balance=models.IntegerField()

    def __str__(self):
        return '%s'%(self.AccountNumber)
        # return '{0}'.format(self.AccountNumber)
        # return str(self.AccountNumber)
