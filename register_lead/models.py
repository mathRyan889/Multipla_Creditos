from django.db import models


class Service(models.Model):
    type_service = models.CharField(max_length=100, verbose_name="Tipo de Serviço", unique=True)
    description = models.TextField(verbose_name="Descrição", blank=True, null=True)

    def __str__(self):
        return self.type_service


class RegisterLead(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    whatsapp = models.CharField(max_length=20, verbose_name="WhatsApp")
    cpf = models.CharField(max_length=15,blank=True,null=True, verbose_name="CPF")
    services = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Serviço")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        ordering = ['services']
        verbose_name = "Registro de Lead"
        verbose_name_plural = "Registros de Leads"

    def __str__(self):
        return f"{self.name} - {self.services.type_service}"