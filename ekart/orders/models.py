from django.db import models
from customers.models import Customer
from products.models import Products

# Order Model

class Orders(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))

    Cart_Stage = 1
    Order_Confirmed = 2
    Order_Processed = 3
    Order_Deleverd = 4
    Order_Rejected = 5
    Order_Status_choices = ((Order_Processed,"Order_Processed"),(Order_Deleverd,"Order_Deleverd"),(Order_Rejected,"Order_Rejected"))

    order_status = models.IntegerField(choices=Order_Status_choices,default=Cart_Stage)



    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name="orders")


class OrderedItems(models.Model):
    product = models.ForeignKey(Products,on_delete=models.SET_NULL,null=True,related_name="added_carts")
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Orders,on_delete=models.SET_NULL,null=True,related_name="added_items")






