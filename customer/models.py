from pyexpat import model
from django.db import models
# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=200,null=False,blank=False)
    customer_email = models.EmailField(unique=True,null=False,blank=False)
    customer_mobile = models.CharField(max_length=12)
    customer_address = models.TextField()
    
    def __str__(self):
        return (self.customer_name)