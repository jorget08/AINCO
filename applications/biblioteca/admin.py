from django.contrib import admin

from .models import Bilbio

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class BilbioResource(resources.ModelResource):
    class Meta:
        model = Bilbio

class BilbioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = BilbioResource

admin.site.register(Bilbio, BilbioAdmin)