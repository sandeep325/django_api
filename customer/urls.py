import imp
from django.urls import path,include
from . import views
urlpatterns1 = [
  
         path('customer_api_urls/', views.apioverview,name="apioverview"),
         path('customer-list/', views.customerList,name="customer-list"),
          path('customer-detail/<int:pk>', views.customerDetail,name="customer-detail"),
          path('customer-create/', views.customerCreate,name="customer-create"),
          path('customer-update/<int:pk>',views.customerUpdate,name="customer-update"),
          path('customer-delete/<int:pk>',views.customerDelete,name="customer-delete")
          
          
    
  ]