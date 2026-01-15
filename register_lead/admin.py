from django.contrib import admin
from .models import RegisterLead, Service

class RegisterLeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'whatsapp', 'cpf', 'services', 'created_at', 'updated_at')
    search_fields = ('name', 'whatsapp', 'cpf')
    list_filter = ('services', 'created_at')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('type_service', 'description')
    search_fields = ('type_service',)

admin.site.register(RegisterLead, RegisterLeadAdmin)
admin.site.register(Service, ServiceAdmin)