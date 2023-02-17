from django.contrib import admin

from .models import EmpresaSocia

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class EmpresaSociaResource(resources.ModelResource):
    class Meta:
        model = EmpresaSocia

class EmpresaSociaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EmpresaSociaResource

admin.site.register(EmpresaSocia, EmpresaSociaAdmin)