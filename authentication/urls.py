from django.urls import path
from .views import *

urlpatterns = [
    path('',Login),
    path('logout/',logoutuser),
    path('signup/',signup),
]