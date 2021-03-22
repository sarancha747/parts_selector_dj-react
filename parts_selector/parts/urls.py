from django.urls import path, include
from .views import socket_list, socket_detail

urlpatterns = [
    path('sockets/', socket_list),
    path('sockets/<int:pk>', socket_detail)
]
