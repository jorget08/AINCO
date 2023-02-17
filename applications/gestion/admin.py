from django.contrib import admin

from .models import Gestion

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class GestionResource(resources.ModelResource):
    class Meta:
        model = Gestion

class GestionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = GestionResource
    readonly_fields = ('fecha_gestion',)

admin.site.register(Gestion, GestionAdmin)