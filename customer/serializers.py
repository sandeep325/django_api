from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
from .models import Customer

class customerserializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','customer_name','customer_email','customer_mobile','customer_address')