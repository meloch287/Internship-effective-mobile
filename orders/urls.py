from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create/', views.order_create, name='order_create'),
    path('delete/<int:order_id>/', views.order_delete, name='order_delete'),
    path('update-status/<int:order_id>/', views.order_update_status, name='order_update_status'),
]
