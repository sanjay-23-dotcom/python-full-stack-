from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *


def Login(request):

    if request.user.is_authenticated:
         
         return redirect('/firstapp/products')


    context =  {

        "error" : ""
    }
     
     
    if request.method == 'POST':
          
          print(request.POST)

          user = authenticate(username = request.POST['username'],password = request.POST['password'])

          print(user)

          if user is not None:
               
               login(request,user)

               return redirect('/orders/customers/')
          
          else:
               
               context= {
                    "error" : "*Invalid username or password"
               }

               return render (request,'Login.html',context)

    return render(request,'Login.html',context)

def logoutuser(request):
     
     logout(request)

     return redirect('/')


def signup(request):

    if request.method == 'POST':
        print(request.POST)

        username = request.POST.get('username')

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {
                "error": "Username already exists"
            })

        new_user = User(
            username=username,
            first_name=request.POST.get('firstname'),
            last_name=request.POST.get('lastname'),
            email=request.POST.get('email_address')
        )

        new_user.set_password(request.POST.get('password'))
        new_user.save()

        return redirect('/')

    return render(request, 'signup.html')


