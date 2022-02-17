import imp
from django.urls import path,include
from . import views
# from customer.urls import urlpatterns1
from customer.urls import urlpatterns1
urlpatterns = [
    path('', views.apioverview,name="apioverview"),
    path('product-list/', views.showAll,name="product-list"),
    path('product-detail/<int:pk>', views.viewproduct,name="product-detail"),
    path('product-create/', views.createProduct,name="product-create"),
    path('product-update/<int:pk>',views.updateProduct,name="product-update"),
    path('product-delete/<int:pk>',views.deleteProduct,name="product-delete"),
    path('product-delete/<int:pk>',views.deleteProduct,name="product-delete"),
    
      
]



