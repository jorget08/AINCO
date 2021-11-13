from django.contrib import admin

from .models import Adicionado

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class AdicionadoResource(resources.ModelResource):
    class Meta:
        model = Adicionado

class AdicionadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = AdicionadoResource

admin.site.register(Adicionado, AdicionadoAdmin)