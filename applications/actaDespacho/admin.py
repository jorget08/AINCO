from django.contrib import admin

from .models import ActaDespacho

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ActaDespachoResource(resources.ModelResource):
    class Meta:
        model = ActaDespacho

class ActaDespachoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ActaDespachoResource

admin.site.register(ActaDespacho, ActaDespachoAdmin)