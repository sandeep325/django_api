from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
from .models import Product

class productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','price','description','stars')