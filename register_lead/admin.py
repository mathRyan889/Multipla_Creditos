import openpyxl
from django.http import HttpResponse
from django.contrib import admin
from .models import RegisterLead, Service

@admin.action(description="Exportar Leads selecionados para Excel")
def exportar_leads_excel(modeladmin, request, queryset):
    # Cria o arquivo Excel
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = "Leads"

    # Define os cabeçalhos personalizados
    columns = ['Nome', 'WhatsApp', 'CPF', 'Serviço', 'Criado em', 'Atualizado em']
    worksheet.append(columns)

    # Itera sobre os leads selecionados
    for lead in queryset:
        # Lógica para tratar o campo 'services' (se for ManyToMany ou ForeignKey)
        # Se for ManyToMany, usamos join para listar todos. Se for ForeignKey, apenas o nome.
        try:
            # Caso seja ManyToMany
            service_display = ", ".join([str(s) for s in lead.services.all()])
        except AttributeError:
            # Caso seja ForeignKey ou um campo simples
            service_display = str(lead.services) if lead.services else ""

        row = [
            lead.name,
            lead.whatsapp,
            lead.cpf,
            service_display,
            lead.created_at.replace(tzinfo=None) if lead.created_at else "",
            lead.updated_at.replace(tzinfo=None) if lead.updated_at else "",
        ]
        worksheet.append(row)

    # Configura a resposta HTTP
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = "attachment; filename=leads_exportados.xlsx"
    
    workbook.save(response)
    return response


@admin.register(RegisterLead)
class RegisterLeadAdmin(admin.ModelAdmin):
    # Organiza as colunas de forma legível
    list_display = ('name', 'whatsapp', 'cpf', 'services', 'created_at')
    
    # Adiciona cores aos itens clicáveis e filtros rápidos
    list_display_links = ('name',)
    search_fields = ('name', 'whatsapp', 'cpf')
    list_filter = ('services', 'created_at')
    
    # Define como datas vazias ou campos nulos aparecem
    empty_value_display = "- não informado -"
    
    actions = [exportar_leads_excel]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('type_service', 'description')
    search_fields = ('type_service',)
    list_filter = ('type_service',)