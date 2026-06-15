from django.urls import path
from .views import *

urlpatterns = [
    path('product/add/',Productsadd),
    path('product/',All_product),
    path('product/delete/<int:id>',Deleteproduct,name='product_delete'),
    path('product/update/<int:id>',Updateproduct,name='product_update'),

    #path('product/add/',Productsaddview.as_view()),
    #path('product/',All_productview.as_view()),
    #path('product/delete/<int:id>',Deleteproductview.as_view,name='product_delete'),
    #path('product/update/<int:id>',ProductUpdateview.as_view,name='product_update'),

]