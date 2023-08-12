"""
URL configuration for zomato_App_main project.

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
from django.contrib import admin
from django.urls import path
from zomato import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='welcome'),
    path('menu/', views.menu, name='menu'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('remove_dish/<int:dish_id>/', views.remove_dish, name='remove_dish'),
    path('update_availability/<int:dish_id>/', views.update_availability, name='update_availability'),
    path('home/', views.home, name='home'),
    path('take_order/', views.take_order, name='take_order'),
    path('orders/', views.my_orders, name='orders'),
     path('update_order_status/<int:order_id>/<str:new_status>/', views.update_order_status, name='update_order_status'),
]

