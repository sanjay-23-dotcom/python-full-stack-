from django.db import models
from firstapp.models import*

class Customer(models.Model):

    customer_name = models.CharField(max_length=200,null=True)
    customer_since =models.DateField(max_length=200,null=True)

    def __str__(self):
        return self.customer_name

class Orders(models.Model):

    Customer_reference = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    Product_reference = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order_number = models.CharField(max_length=20,null=True)
    order_date = models.DateField(null=True)
    quantity = models.FloatField(null=True)
    amount =  models.FloatField(null=True)
    gst_amount =  models.FloatField(null=True)
    bill_amount =  models.FloatField(null=True)

    def __str__(self):
        return self.order_number




