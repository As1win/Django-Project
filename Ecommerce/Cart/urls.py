"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Cart import views
app_name='Cart'

from django.urls import path,include

urlpatterns = [
     path('Cart/<p>', views.Add_to_cart, name="Add_to_cart"),
     path('Cart_view', views.Cart_view, name="Cart_view"),
     path('Cart_remove/<p>', views.Cart_remove, name="Cart_remove"),
     path('Full_remove/<p>', views.Full_remove, name="Full_remove"),
     path('Order_form/', views.Order_form, name="Order_form"),
     path('Orders/', views.Orders, name="Orders"),

]

