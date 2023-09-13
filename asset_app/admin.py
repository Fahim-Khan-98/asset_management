from django.contrib import admin
from asset_app.models import Company, CompanyEmployee, Asset, Delegation

# Register your models here.
class DelegationAdmin(admin.ModelAdmin):
    list_display = ('id', 'asset', 'assigned_to', 'start_date', 'created_by', 'updated_by')

admin.site.register(Delegation, DelegationAdmin)


class AssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'created_by', 'created_at', 'updated_by', 'updated_at')
    search_fields = ('name','company__name',)
    readonly_fields = ('created_by', 'created_at', 'updated_by', 'updated_at')

    filter_horizontal = ()
    # filter_vertical = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Asset, AssetAdmin)

class CompanyEmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'company', 'created_by', 'created_at', 'updated_by', 'updated_at')

admin.site.register(CompanyEmployee, CompanyEmployeeAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by', 'created_at', 'updated_by', 'updated_at')

admin.site.register(Company, CompanyAdmin)