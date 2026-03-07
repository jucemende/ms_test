from django.urls import path
from .views import lista_clientes, inativar_cliente, reativar_cliente

urlpatterns = [
    path("", lista_clientes, name="lista_clientes"),
    path("clientes/<int:cliente_id>/inativar/", inativar_cliente, name="inativar_cliente"),
    path("clientes/<int:cliente_id>/reativar/", reativar_cliente, name="reativar_cliente"),
]