from django.shortcuts import render, redirect, get_object_or_404
from .models import*
from .forms import*
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def CustomerList(request):
    context = {
        'all_customers': Customer.objects.all()
    }
    return render(request, 'ordermanagement/customer_list.html', context)

@login_required(login_url='/')
def CustomerAdd(request):
    form = CustomerForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('customer_list')

    return render(request, 'ordermanagement/customer_add.html', {
        'customer_form': form,
        'is_update': False
    })

@login_required(login_url='/')
def CustomerUpdate(request, id):
    customer = get_object_or_404(Customer, id=id)
    form = CustomerForm(request.POST or None, instance=customer)

    if form.is_valid():
        form.save()
        return redirect('customer_list')

    return render(request, 'ordermanagement/customer_add.html', {
        'customer_form': form,
        'is_update': True
    })

@login_required(login_url='/')
def CustomerDelete(request, id):
    customer = get_object_or_404(Customer, id=id)
    customer.delete()
    return redirect('customer_list')

@login_required(login_url='/')
def OrdersAdd(request):

    context = {
        'orders_form': OrdersForm()
    }

    if request.method == 'POST':

        selected_product = Product.objects.get(
            id=request.POST['Product_reference']
        )

        amount = float(selected_product.price) * float(request.POST['quantity'])
        gst_amount = (amount * selected_product.gst) / 100
        bill_amount = amount + gst_amount

        new_order = Orders(
            Customer_reference_id=request.POST['Customer_reference'],
            Product_reference_id=request.POST['Product_reference'],
            order_number=request.POST['order_number'],
            order_date=request.POST['order_date'],
            quantity=request.POST['quantity'],
            amount=amount,
            gst_amount=gst_amount,
            bill_amount=bill_amount
        )

        new_order.save()

    return render(request, 'ordermanagement/orders_add.html', context)

@login_required(login_url='/')
def Orderslist (request):

    context = {
        'all_orders' : Orders.objects.all()
         
    }

    return render (request,'ordermanagement/orderlist.html',context)

@login_required(login_url='/')
def OrderDelete (request,id):

   order =  Orders.objects.get(id=id)
   
   order.delete()

   return redirect('/orders/orderlist/')

@login_required(login_url='/')
def OrderUpdate(request, id):

    order = get_object_or_404(Orders, id=id)

    if request.method == 'POST':
        form = OrdersForm(request.POST, instance=order)

        if form.is_valid():
          
            selected_product = form.cleaned_data.get('product_reference')
            quantity = form.cleaned_data.get('quantity')

            
            if not selected_product or not quantity:
                return render(request, 'ordermanagement/orders_add.html', {
                    'orders_form': form,
                    'error': 'Invalid product or quantity'
                })

         
            amount = selected_product.price * quantity
            gst_amount = (amount * selected_product.gst) / 100
            bill_amount = amount + gst_amount

            order = form.save(commit=False)
            order.amount = amount
            order.gst_amount = gst_amount
            order.bill_amount = bill_amount
            order.save()

            return redirect('orders/orderlist')

        else:
    
            return render(request, 'ordermanagement/orders_add.html', {
                'orders_form': form
            })

    else:
        form = OrdersForm(instance=order)

    return render(request, 'ordermanagement/orders_add.html', {
        'orders_form': form
    })
