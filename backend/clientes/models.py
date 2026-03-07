from django.db import models


class TipoCliente(models.TextChoices):
    PESSOA_FISICA = "PF", "Pessoa Física"
    PESSOA_JURIDICA = "PJ", "Pessoa Jurídica"
    VIP = "VIP", "VIP"


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    tipo = models.CharField(
        max_length=3,
        choices=TipoCliente.choices,
        default=TipoCliente.PESSOA_FISICA,
    )
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome
