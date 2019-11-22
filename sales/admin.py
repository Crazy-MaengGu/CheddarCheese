from django.contrib import admin
from .models import SalesType, SalesIndustryType, Contract, ContractManager, Revenue, Purchase, Category, ContractItem, Goal


@admin.register(SalesType)
class SalesTypeAdmin(admin.ModelAdmin):
    list_display = ('sal_type_id', 'sal_type_comt')
    list_filter = ('sal_type_id', 'sal_type_comt')
    list_display_links = ['sal_type_id', 'sal_type_comt']


@admin.register(SalesIndustryType)
class SalesIndustryTypeAdmin(admin.ModelAdmin):
    list_display = ('sal_industry_id', 'sal_industry_comt')
    list_filter = ('sal_industry_id', 'sal_industry_comt')
    list_display_links = ['sal_industry_id', 'sal_industry_comt']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('cont_id', 'cont_name', 'cont_emp_name', 'cont_emp_dept_name', 'cont_sal_type_id', 'cont_sal_industry_id', 'cont_cate_main', 'cont_cate_sub')
    list_filter = ('cont_id', 'cont_name', 'cont_emp_dept_name', 'cont_sal_type_id', 'cont_sal_industry_id')
    list_display_links = ['cont_id', 'cont_name', 'cont_emp_name', 'cont_emp_dept_name', 'cont_sal_type_id', 'cont_sal_industry_id', 'cont_cate_main', 'cont_cate_sub']


@admin.register(ContractManager)
class ContractManagerAdmin(admin.ModelAdmin):
    list_display = ('cont_mng_id', 'cont_mng_cont_id', 'cont_mng_emp_id', 'cont_mng_date', 'cont_mng_sal_price', 'cont_mng_cust_id')
    list_filter = ('cont_mng_id', 'cont_mng_cont_id', 'cont_mng_sal_price', 'cont_mng_cust_id')
    list_display_links = ['cont_mng_id', 'cont_mng_cont_id', 'cont_mng_emp_id', 'cont_mng_date', 'cont_mng_sal_price', 'cont_mng_cust_id']


@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    list_display = ('reve_id', 'reve_cont_id', 'reve_emp_id', 'reve_seq', 'reve_comt', 'reve_com_id')
    list_filter = ('reve_id', 'reve_cont_id', 'reve_emp_id', 'reve_com_id')
    list_display_links = ['reve_id', 'reve_cont_id', 'reve_emp_id', 'reve_seq', 'reve_comt', 'reve_com_id']


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('purc_id', 'purc_cont_id', 'purc_emp_id', 'purc_seq', 'purc_comt', 'purc_com_id')
    list_filter = ('purc_id', 'purc_cont_id', 'purc_emp_id', 'purc_com_id')
    list_display_links = ['purc_id', 'purc_cont_id', 'purc_emp_id', 'purc_seq', 'purc_comt', 'purc_com_id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cate_id', 'cate_comt', 'cate_depen_id')
    list_filter = ('cate_id', 'cate_comt', 'cate_depen_id')
    list_display_links = ['cate_id', 'cate_comt', 'cate_depen_id']


@admin.register(ContractItem)
class ContractItemAdmin(admin.ModelAdmin):
    list_display = ('cont_item_id', 'cont_item_cont_id', 'cont_item_cate_id', 'cont_item_seq', 'cont_item_comt')
    list_filter = ('cont_item_id', 'cont_item_cont_id', 'cont_item_cate_id')
    list_display_links = ['cont_item_id', 'cont_item_cont_id', 'cont_item_cate_id', 'cont_item_seq', 'cont_item_comt']


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('goal_id', 'goal_dept_id', 'goal_emp_id', 'year', 'year_sales_sum')
    list_filter = ('goal_id', 'goal_dept_id', 'goal_emp_id', 'year', 'year_sales_sum')
    list_display_links = ['goal_id', 'goal_dept_id', 'goal_emp_id', 'year', 'year_sales_sum']
