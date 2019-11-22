from django.contrib import admin
from .models import Company, Customer, SupportHistory, CompanyInfo, CompanyInfoDetail



@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('com_id', 'com_name', 'com_name_ko', 'com_addr', 'com_stat')
    list_filter = ('com_id', 'com_name', 'com_name_ko', 'com_stat')
    list_display_links = ['com_id', 'com_name', 'com_name_ko', 'com_addr', 'com_stat']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('cust_id', 'cust_name', 'cust_dept_name', 'cust_stat', 'cust_com_id')
    list_display_links = ['cust_id', 'cust_name', 'cust_stat', 'cust_com_id']
    list_filter = ('cust_id', 'cust_name', 'cust_dept_name', 'cust_stat', 'cust_com_id')

@admin.register(SupportHistory)
class SupportHistoryAdmin(admin.ModelAdmin):
    list_display = ('sup_hist_id', 'sup_hist_emp_id', 'sup_hist_com_id', 'sup_hist_type', 'sup_hist_start_date', 'sup_hist_end_date')
    list_display_links = ['sup_hist_id', 'sup_hist_emp_id', 'sup_hist_com_id', 'sup_hist_type']
    list_filter = ('sup_hist_id', 'sup_hist_emp_id', 'sup_hist_com_id', 'sup_hist_type', 'sup_hist_start_date', 'sup_hist_end_date')


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('com_info_id', 'com_info_com_id', 'com_info_seq', 'com_info_attribute', 'com_info_attribute_comt')
    list_display_links = ['com_info_id', 'com_info_com_id', 'com_info_attribute']
    list_filter = ('com_info_id', 'com_info_com_id', 'com_info_seq', 'com_info_attribute', 'com_info_attribute_comt')


@admin.register(CompanyInfoDetail)
class CompanyInfoDetailAdmin(admin.ModelAdmin):
    list_display = ('com_info_det_id', 'com_info_det_com_id', 'com_info_det_com_info_id', 'com_info_det_seq', 'com_info_det_comt')
    list_display_links = ['com_info_det_id', 'com_info_det_com_id', 'com_info_det_comt']
    list_filter = ('com_info_det_id', 'com_info_det_com_id', 'com_info_det_com_info_id', 'com_info_det_seq', 'com_info_det_comt')

