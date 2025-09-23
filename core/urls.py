# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contato/', views.pagina_contato, name='contato'), # URL para a página de contato
]