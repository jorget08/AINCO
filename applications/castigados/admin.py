from django.contrib import admin

from .models import CastigoCartera

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CastigoCarteraResource(resources.ModelResource):
    class Meta:
        model = CastigoCartera

class CastigoCarteraAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CastigoCarteraResource

admin.site.register(CastigoCartera, CastigoCarteraAdmin)