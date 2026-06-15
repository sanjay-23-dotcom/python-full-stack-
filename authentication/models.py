from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    age = models.ImageField(default=0),
    name = models.CharField(max_length=100),
    
    role_choices =(
    (0,'admin'),
    (1,'manager'),
    (2,'employee')
)


    role = models.IntegerField(default=0,choices = role_choices)



