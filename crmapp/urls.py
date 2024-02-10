from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
      path('home',views.home,name='home'),
      path('firstpage',views.firstpage,name='firstpage'),
      path('contact',views.contact,name='contact'),
            path('deals',views.deals,name='deals'),



   





]