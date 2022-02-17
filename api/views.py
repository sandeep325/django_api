from itertools import product
from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api import serializers
# Create your views here.
from  api.serializers import productserializer
from .models import Product
from rest_framework import status

@api_view(['GET'])
def apioverview(request):
    api_urls = {
    'List':'/product-list',
     'Detail view':'/product-detail/<int:id>',
     'create': '/product-create',   
        'update':'/product-update/<int:id>',
        'delete':'/product-delete/<int:id>',
    }
    return Response(api_urls)

@api_view(['GET'])
def showAll(request):
    
    products = Product.objects.all()
    serializer = productserializer(products,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def viewproduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = productserializer(product,many=False)
    return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['POST'])
def createProduct(request):
    serializer = productserializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED) 
    
    
    
@api_view(['put'])
def updateProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = productserializer(instance=product,data = request.data)
    if serializer.is_valid():
     serializer.save()
     return Response(serializer.data,status=status.HTTP_200_OK)
        
@api_view(['delete'])
def deleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response("Product Delete successfully...",status=status.HTTP_200_OK)
    
    
            
        
        
    
    