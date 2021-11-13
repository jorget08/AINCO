from django.contrib import admin

from .models import AcuerdosPago

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class AcuerdosPagoResource(resources.ModelResource):
    class Meta:
        model = AcuerdosPago

class AcuerdosPagoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = AcuerdosPagoResource

admin.site.register(AcuerdosPago, AcuerdosPagoAdmin)