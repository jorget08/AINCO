from django.contrib import admin

from .models import Pagos

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class PagosResource(resources.ModelResource):
    class Meta:
        model = Pagos

class PagosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PagosResource

admin.site.register(Pagos, PagosAdmin)