from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('order_list', permanent=False)),
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls')),
]
