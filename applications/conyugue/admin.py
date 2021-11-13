from django.contrib import admin

from .models import Conyugue

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ConyugueResource(resources.ModelResource):
    class Meta:
        model = Conyugue

class ConyugueAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ConyugueResource

admin.site.register(Conyugue, ConyugueAdmin)