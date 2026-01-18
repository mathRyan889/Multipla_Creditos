import openpyxl
from django.http import HttpResponse
from django.contrib import admin
from django.utils.html import format_html # Importado para criar o link do WhatsApp
from .models import RegisterLead, Service

@admin.action(description="📥 Exportar selecionados para Excel")
def exportar_leads_excel(modeladmin, request, queryset):
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = "Leads"

    columns = ['Nome', 'WhatsApp', 'CPF', 'Serviço', 'Criado em', 'Atualizado em']
    worksheet.append(columns)

    for lead in queryset:
        try:
            service_display = ", ".join([str(s) for s in lead.services.all()])
        except AttributeError:
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

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = "attachment; filename=leads_exportados.xlsx"
    
    workbook.save(response)
    return response

@admin.register(RegisterLead)
class RegisterLeadAdmin(admin.ModelAdmin):
    # UX: whatsapp_link adicionado para contato rápido sem sair da página
    list_display = ('name', 'whatsapp_link', 'cpf', 'services', 'created_at')
    list_display_links = ('name',)
    search_fields = ('name', 'whatsapp', 'cpf')
    list_filter = ('services', 'created_at')
    empty_value_display = "- não informado -"
    actions = [exportar_leads_excel]

    # Função para criar o botão de WhatsApp direto na lista de Leads
    def whatsapp_link(self, obj):
        # Remove caracteres não numéricos para o link do wa.me
        clean_phone = "".join(filter(str.isdigit, obj.whatsapp))
        return format_html(
            '<a href="https://wa.me/55{}" target="_blank" style="'
            'background-color: #25D366; color: white; padding: 5px 10px; '
            'border-radius: 5px; text-decoration: none; font-weight: bold; font-size: 12px;">'
            '<i class="fab fa-whatsapp"></i> {}</a>',
            clean_phone, obj.whatsapp
        )
    whatsapp_link.short_description = "WhatsApp (Contato Direto)"

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('type_service', 'description')
    search_fields = ('type_service',)
    list_filter = ('type_service',)

