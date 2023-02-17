from django.contrib import admin
from .models import Credito

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CreditoResource(resources.ModelResource):
    class Meta:
        model = Credito
        import_id_fields = ('codigo_credito',)

class CreditoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CreditoResource

admin.site.register(Credito, CreditoAdmin)