from django.urls import path
from .views import *


urlpatterns = [
    path('customers/', CustomerList, name='customer_list'),
    path('customers/add/', CustomerAdd, name='customer_add'),
    path('customers/update/<int:id>/', CustomerUpdate, name='customer_update'),
    path('customers/delete/<int:id>/', CustomerDelete, name='customer_delete'),
    
    
    path('add/orders/',OrdersAdd),
    path('orderlist/',Orderslist),
    path('delete/orders/<int:id>/',OrderDelete, name='order_delete'),
    path('update/orders/<int:id>/',OrderUpdate, name='order_update')
]