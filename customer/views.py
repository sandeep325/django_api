from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework import status
from api import serializers
from customer.serializers import customerserializer
import customer
from customer.models import Customer

@api_view(['GET'])
def apioverview(request):
    api_urls = {
    'List':'/customer-list',
     'Detail view':'/customer-detail/<int:id>',
     'create': '/customer-create',   
        'update':'/customer-update/<int:id>',
        'delete':'/customer-delete/<int:id>',
    }
    return Response(api_urls)

@api_view(['GET'])
def customerList(request):
    
    customer = Customer.objects.all()
    serializer = customerserializer(customer,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def customerDetail(request,pk):
    customerDetail = Customer.objects.get(id=pk)
    serializer = customerserializer(customerDetail,many=False)
    return Response(serializer.data,status=status.HTTP_200_OK)
    

@api_view(['POST'])   
def customerCreate(request):
     serializer = customerserializer(data = request.data) 
     
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED) 
    
@api_view(['put'])
def customerUpdate(request,pk):
    customerDetail = Customer.objects.get(id=pk)
    serialize_data = customerserializer(instance=customerDetail,data=request.data)
    if serialize_data.is_valid():
        serialize_data.save()
        return Response(serialize_data.data,status=status.HTTP_200_OK)
    
    
@api_view(['delete'])
def customerDelete(request,pk):
    customerdel = Customer.objects.get(id=pk)
    customerdel.delete()
    return Response("Customer Delete successfully...",status=status.HTTP_200_OK)    
        