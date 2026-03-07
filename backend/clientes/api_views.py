from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Cliente
from .serializers import ClienteSerializer


@api_view(["GET"])
def listar_clientes(request):
    mostrar_inativos = request.GET.get("mostrar_inativos") == "1"

    if mostrar_inativos:
        clientes = Cliente.objects.all()
    else:
        clientes = Cliente.objects.filter(ativo=True)

    serializer = ClienteSerializer(clientes, many=True)
    return Response(serializer.data)

@api_view(["PATCH"])
def inativar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.ativo = False
    cliente.save(update_fields=["ativo"])
    return Response({"status": "cliente inativado"})


@api_view(["PATCH"])
def reativar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.ativo = True
    cliente.save(update_fields=["ativo"])
    return Response({"status": "cliente reativado"})