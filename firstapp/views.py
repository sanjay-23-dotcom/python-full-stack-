from django.shortcuts import render,redirect
from .forms import *
from .models import * 
from django.views import View
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin

@login_required(login_url='/')
def Productsadd(request):

    context={
        'product_form':Product_form()
    }

    if request.method == "POST":

        product_form = Product_form(request.POST)

        if product_form.is_valid():

            product_form.save()



    return render(request,'products_add.html',context)

@login_required(login_url='/')
def All_product(request):

    context = {
        'all_product': Product.objects.all()
    }

    return render(request, 'product.html', context)

@login_required(login_url='/')
def Deleteproduct(request,id):

    Selected_product = Product.objects.get(id = id)

    Selected_product.delete()

    return redirect ('/firstapp/product/')

@login_required(login_url='/')
def Updateproduct(request,id):

    Selected_product = Product.objects.get(id = id)

    context = {
        "product_form" : Product_form(instance=Selected_product)
    }

    if request.method == 'POST':

        product_form = Product_form(request.POST, instance=Selected_product)

        if product_form.is_valid():
            
            product_form.save()

            return redirect ('/firstapp/product/')

    return render (request,'products_add.html',context)



class Productsaddview(View):

    def get(self,request):


        print(" from class based get")

        context={
        'product_form':Product_form()
    }
        
        return render(request,'products_add.html',context)
    
    def post(self,request):

        print("from class based post")

        product_form = Product_form(request.POST)

        if product_form.is_valid():

            product_form.save()

class All_productview(View):

    def get(self,request):

         context = {
        'all_product': Product.objects.all()
    }
         
         return render(request, 'product.html', context)

class Deleteproductview(View):
     
     def get(self,request,id):
         
         Selected_product = Product.objects.get(id = id)
         
         Selected_product.delete()
         
         return redirect ('/firstapp/product/')
     
class ProductUpdateview (View):

    def get(self,request,id):

         Selected_product = Product.objects.get(id = id)
         
         context = {
             
             "product_form" : Product_form(instance=Selected_product)
    }
         
         return render (request,'products_add.html',context)
         
    def post(self,request,id):
        
        Selected_product = Product.objects.get(id = id)
        
        product_form = Product_form(request.POST, instance=Selected_product)

        if product_form.is_valid():
            
            product_form.save()

            return redirect ('/firstapp/product/')
        
        







     

     
     



    








