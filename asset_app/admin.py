from django.contrib import admin
from asset_app.models import Company, CompanyEmployee, Asset, Delegation

# Register your models here.
admin.site.register(Delegation)


class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'created_by', 'created_at', 'updated_by', 'updated_at')

admin.site.register(Asset, AssetAdmin)

class CompanyEmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'company', 'created_by', 'created_at', 'updated_by', 'updated_at')

admin.site.register(CompanyEmployee, CompanyEmployeeAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at', 'updated_by', 'updated_at')

admin.site.register(Company, CompanyAdmin)