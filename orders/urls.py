from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.pagina_orders, name = 'orders'),
]
