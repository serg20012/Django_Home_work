from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('all_order/<int:client_id>/', views.all_order, name='all_order'),
    path('all_product/<int:client_id>/', views.client_products, name='client_products'),
]