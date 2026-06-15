from django import forms
from .models import*

class CustomerForm(forms.ModelForm):
    class Meta:

        
        model = Customer
        fields = '__all__'

class OrdersForm(forms.ModelForm):

    class Meta:


        model = Orders 
        fields = ['Customer_reference','Product_reference','order_number','order_date','quantity']