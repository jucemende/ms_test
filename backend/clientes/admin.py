from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "email", "tipo", "criado_em")
    search_fields = ("nome", "email")
    list_filter = ("tipo",)
