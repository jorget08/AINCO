from django.contrib import admin

from .models import Codeudor

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CodeudorResource(resources.ModelResource):
    class Meta:
        model = Codeudor
        import_id_fields = ('cedula',)

class CodeudorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CodeudorResource

admin.site.register(Codeudor, CodeudorAdmin)