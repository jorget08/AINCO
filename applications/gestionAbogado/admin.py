from django.contrib import admin

from .models import GestionAbogado

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class GestionAbogadoResource(resources.ModelResource):
    class Meta:
        model = GestionAbogado

class GestionAbogadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = GestionAbogadoResource

admin.site.register(GestionAbogado, GestionAbogadoAdmin)