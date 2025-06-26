from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_cliente, name='cadastro_cliente'),
    path('', views.lista_clientes, name='lista_clientes'),
]
