"""retailstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from retailers import views
urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls),
    path('std/', views.std),
    path('items/', views.items),
    path('cust/', views.cust),
    path('customers/', views.customers),
    path('delete_cust/<int:id>',views.delete_cust),
    path('cart/', views.cart),
    path('delete_cart/<int:id>', views.delete_cart),
    path('update_cart/<int:id>', views.update_cart),
    path('cart_contains', views.cart_contains),
    path('order_details',views.order_details),
    path('developer', views.developer)
]
