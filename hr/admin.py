from django.contrib import admin
from .models import Position, Department, Employee, EmployeeHistory, Attendance, Punctuality, PayHistory


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('posit_id', 'posit_name', 'posit_salary')
    list_filter = ('posit_id', 'posit_name', 'posit_salary')
    list_display_links = ['posit_id', 'posit_name', 'posit_salary']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_id', 'dept_name', 'dept_depen_id', 'dept_emp_id')
    list_filter = ('dept_id', 'dept_name')
    list_display_links = ['dept_id', 'dept_name', 'dept_depen_id', 'dept_emp_id']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'emp_name', 'emp_phone', 'emp_email', 'emp_stat', 'emp_type', 'emp_mng')
    list_filter = ('emp_id', 'emp_name', 'emp_stat', 'emp_type', 'emp_mng')
    list_display_links = ['emp_id', 'emp_name', 'emp_phone', 'emp_email', 'emp_stat', 'emp_type', 'emp_mng']

@admin.register(EmployeeHistory)
class EmployeeHistoryAdmin(admin.ModelAdmin):
    list_display = ('emp_hist_id', 'emp_hist_emp_id', 'emp_hist_start_date', 'emp_hist_end_date', 'emp_hist_type')
    list_filter = ('emp_hist_id', 'emp_hist_emp_id', 'emp_hist_type')
    list_display_links = ['emp_hist_id', 'emp_hist_emp_id', 'emp_hist_start_date', 'emp_hist_end_date', 'emp_hist_type']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('attd_id', 'attd_date', 'attd_time', 'attd_type', 'attd_emp_id')
    list_filter = ('attd_id', 'attd_date', 'attd_type', 'attd_emp_id')
    list_display_links = ['attd_id', 'attd_date', 'attd_time', 'attd_type', 'attd_emp_id']

@admin.register(Punctuality)
class PunctualityAdmin(admin.ModelAdmin):
    list_display = ('punc_id', 'punc_date', 'punc_type', 'punc_comt', 'punc_emp_id')
    list_filter = ('punc_id', 'punc_date', 'punc_type', 'punc_emp_id')
    list_display_links = ['punc_id', 'punc_date', 'punc_type', 'punc_comt', 'punc_emp_id']

@admin.register(PayHistory)
class PayHistoryAdmin(admin.ModelAdmin):
    list_display = ('pay_hist_id', 'pay_hist_emp_id', 'pay_hist_date', 'pay_hist_tot_price', 'pay_hist_default_price', 'pay_hist_etc_price', 'pay_hist_bouns_price')
    list_filter = ('pay_hist_id', 'pay_hist_emp_id', 'pay_hist_date', 'pay_hist_tot_price')
    list_display_links = ['pay_hist_id', 'pay_hist_emp_id', 'pay_hist_date', 'pay_hist_tot_price', 'pay_hist_default_price', 'pay_hist_etc_price', 'pay_hist_bouns_price']

