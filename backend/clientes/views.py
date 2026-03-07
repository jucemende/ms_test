from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente


def lista_clientes(request):
    mostrar_inativos = request.GET.get("mostrar_inativos") == "1"

    if mostrar_inativos:
        clientes = Cliente.objects.all()
    else:
        clientes = Cliente.objects.filter(ativo=True)
    
    return render(request, "clientes/lista_clientes.html", {"clientes": clientes})

def inativar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.ativo = False
    cliente.save(update_fields=["ativo"])
    return redirect("lista_clientes")

def reativar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.ativo = True
    cliente.save(update_fields=["ativo"])
    return redirect("lista_clientes")