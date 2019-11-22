from django.contrib import admin
from .models import PrivilegeDetail, PrivilegeRole, PrivilegeGrant


@admin.register(PrivilegeDetail)
class PrivilegeDetailAdmin(admin.ModelAdmin):
    list_display = ('priv_det_id', 'priv_det_date', 'priv_det_level_type', 'priv_det_comt')
    list_filter = ('priv_det_id', 'priv_det_level_type', 'priv_det_comt')
    list_display_links = ['priv_det_id', 'priv_det_date', 'priv_det_level_type', 'priv_det_comt']


@admin.register(PrivilegeRole)
class PrivilegeRoleAdmin(admin.ModelAdmin):
    list_display = ('priv_role_id', 'priv_role_seq', 'priv_role_det_id', 'priv_role_comt')
    list_filter = ('priv_role_id', 'priv_role_det_id', 'priv_role_comt')
    list_display_links = ['priv_role_id', 'priv_role_seq', 'priv_role_det_id', 'priv_role_comt']


@admin.register(PrivilegeGrant)
class PrivilegeGrantAdmin(admin.ModelAdmin):
    list_display = ('priv_grant_id', 'priv_grant_role_id', 'priv_grant_det_id', 'priv_grant_dept_id', 'priv_grant_emp_id')
    list_filter = ('priv_grant_id', 'priv_grant_role_id', 'priv_grant_det_id', 'priv_grant_dept_id', 'priv_grant_emp_id')
    list_display_links = ['priv_grant_id', 'priv_grant_role_id', 'priv_grant_det_id', 'priv_grant_dept_id', 'priv_grant_emp_id']


