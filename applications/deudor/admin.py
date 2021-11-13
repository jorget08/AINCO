from django.contrib import admin

from .models import Deudor

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class DeudorResource(resources.ModelResource):
    class Meta:
        model = Deudor
        import_id_fields = ('cedula',)

class DeudorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = DeudorResource
    list_display = ('pk', 'cedula', 'full_name')

admin.site.register(Deudor, DeudorAdmin)