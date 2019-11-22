from django.contrib import admin
from .models import ServiceReport, ServiceType, ServiceSupportTime, OvertimeDaysManage, ServiceOvertimeDetail, ServiceWorker, ServiceForm, Vacation


@admin.register(ServiceReport)
class ServiceReportAdmin(admin.ModelAdmin):
    list_display = ('srv_id', 'srv_date', 'srv_stat', 'srv_emp_id', 'srv_com_id', 'srv_srvtype_id', 'srv_cont_id')
    list_filter = ('srv_id', 'srv_date', 'srv_stat', 'srv_emp_id', 'srv_com_id', 'srv_srvtype_id', 'srv_cont_id')
    list_display_links = ['srv_id', 'srv_date', 'srv_stat', 'srv_emp_id', 'srv_com_id', 'srv_srvtype_id', 'srv_cont_id']


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('srv_type_id', 'srv_type_name', 'srv_type_comt')
    list_filter = ('srv_type_id', 'srv_type_name', 'srv_type_comt')
    list_display_links = ['srv_type_id', 'srv_type_name', 'srv_type_comt']


@admin.register(ServiceSupportTime)
class ServiceSupportTimeAdmin(admin.ModelAdmin):
    list_display = ('srv_suptime_id', 'srv_suptime_srv_id', 'srv_suptime_toth', 'srv_suptime_hour', 'srv_suptime_ovh')
    list_filter = ('srv_suptime_id', 'srv_suptime_srv_id', 'srv_suptime_toth', 'srv_suptime_hour', 'srv_suptime_ovh')
    list_display_links = ['srv_suptime_id', 'srv_suptime_srv_id', 'srv_suptime_toth', 'srv_suptime_hour', 'srv_suptime_ovh']


@admin.register(OvertimeDaysManage)
class OvertimeDaysManageAdmin(admin.ModelAdmin):
    list_display = ('ovt_id', 'ovt_date', 'ovt_start_time', 'ovt_end_time', 'ovt_type', 'ovt_comt')
    list_filter = ('ovt_id', 'ovt_date', 'ovt_type')
    list_display_links = ['ovt_id', 'ovt_date', 'ovt_start_time', 'ovt_end_time', 'ovt_type', 'ovt_comt']


@admin.register(ServiceOvertimeDetail)
class ServiceOvertimeDetailAdmin(admin.ModelAdmin):
    list_display = ('ovt_det_id', 'ovt_det_srv_id', 'ovt_det_ovt_id', 'ovt_det_comt')
    list_filter = ('ovt_det_id', 'ovt_det_srv_id', 'ovt_det_ovt_id', 'ovt_det_comt')
    list_display_links = ['ovt_det_id', 'ovt_det_srv_id', 'ovt_det_ovt_id', 'ovt_det_comt']

@admin.register(ServiceWorker)
class ServiceWorkerAdmin(admin.ModelAdmin):
    list_display = ('worker_id', 'worker_srv_id', 'worker_emp_id', 'worker_emp_name')
    list_filter = ('worker_id', 'worker_srv_id', 'worker_emp_id', 'worker_emp_name')
    list_display_links = ['worker_id', 'worker_srv_id', 'worker_emp_id', 'worker_emp_name']

@admin.register(ServiceForm)
class ServiceFormAdmin(admin.ModelAdmin):
    list_display = ('srv_form_id', 'srv_form_emp_id', 'srv_form_com_id', 'srv_form_srvtype_id', 'srv_form_title', 'srv_form_det')
    list_filter = ('srv_form_id', 'srv_form_emp_id', 'srv_form_com_id', 'srv_form_srvtype_id', 'srv_form_title')
    list_display_links = ['srv_form_id', 'srv_form_emp_id', 'srv_form_com_id', 'srv_form_srvtype_id', 'srv_form_title', 'srv_form_det']

@admin.register(Vacation)
class VacationAdmin(admin.ModelAdmin):
    list_display = ('vac_id', 'vac_emp_id', 'vac_date', 'vac_usetype', 'vac_applytype', 'vac_type')
    list_filter = ('vac_id', 'vac_emp_id', 'vac_date', 'vac_usetype', 'vac_applytype', 'vac_type')
    list_display_links = ['vac_id', 'vac_emp_id', 'vac_date', 'vac_usetype', 'vac_applytype', 'vac_type']
