from django.urls import path
from . import api_views

urlpatterns = [
    path("", api_views.listar_clientes),
    path("<int:cliente_id>/inativar/", api_views.inativar_cliente),
    path("<int:cliente_id>/reativar/", api_views.reativar_cliente),
]