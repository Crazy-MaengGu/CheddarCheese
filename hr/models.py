from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Position(models.Model):
    posit_id = models.IntegerField(primary_key=True)
    posit_name = models.CharField(max_length=30)
    posit_salary = models.IntegerField(default=0)

    def __str__(self):
        return self.posit_name


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=30)
    dept_depen_id = models.ForeignKey("hr.Department", on_delete=models.SET_NULL, related_name='dept_dependency_id', null=True)
    dept_emp_id = models.ForeignKey("hr.Employee", on_delete=models.SET_NULL, related_name='dept_emp_id', null=True)

    def __str__(self):
        return self.dept_name


class Employee(models.Model):
    empDeptNameChoices = (
        ('임원', '임원'),
        ('경영지원본부', '경영지원본부'),
        ('영업1팀', '영업1팀'),
        ('영업2팀', '영업2팀'),
        ('영업3팀', '영업3팀'),
        ('인프라서비스사업팀', '인프라서비스사업팀'),
        ('솔루션지원팀', '솔루션지원팀'),
        ('DB지원팀', 'DB지원팀'),
        ('미정', '미정')
    )
    statusChoices = (('Y', 'Y'), ('N', 'N'))

    emp_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emp_code = models.CharField(max_length=20, unique=True)
    emp_name = models.CharField(max_length=30)
    emp_phone = models.CharField(max_length=20)
    emp_email = models.CharField(max_length=254)
    emp_dept_id = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='emp_dept_id', default='미정')
    emp_message = models.CharField(max_length=200, default='내근 업무 내용을 작성해 주세요.', help_text='내근 업무 내용을 작성해 주세요.')
    emp_annaul = models.CharField(max_length=2, default='0')
    emp_stat = models.CharField(max_length=1, choices=statusChoices, default='Y')
    emp_salary = models.IntegerField(default=0)
    emp_vacation_days = models.CharField(max_length=2, default='0')
    emp_type = models.CharField(max_length=2, default='정직원')
    emp_posit_id = models.ForeignKey(Position, on_delete=models.PROTECT, related_name='emp_posit_id')
    emp_mng = models.ForeignKey("hr.Employee", on_delete=models.SET_NULL, related_name='emp_mng_emp_id', null=True)

    def __str__(self):
        return self.emp_name


class EmployeeHistory(models.Model):
    emp_hist_id = models.AutoField(primary_key=True)
    emp_hist_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='emp_hist_emp_id')
    emp_hist_start_date = models.DateField()
    emp_hist_end_date = models.DateField(default='9999-12-31')
    emp_hist_type = models.CharField(max_length=2)
    emp_hist_comt = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = (('emp_hist_emp_id', 'emp_hist_start_date', 'emp_hist_end_date'),)

    def __str__(self):
        return 'Employee History : {} {}'.format(self.emp_id, self.emp_hist_start_date)


class Attendance(models.Model):
    attd_id = models.AutoField(primary_key=True)
    attd_date = models.DateField()
    attd_time = models.TimeField()
    attd_type = models.CharField(max_length=2)
    attd_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attd_emp_id')

    def __str__(self):
        return str(self.attd_date)


class Punctuality(models.Model):
    punc_id = models.AutoField(primary_key=True)
    punc_date = models.DateField()
    punc_type = models.CharField(max_length=2)
    punc_comt = models.CharField(max_length=200, null=True, blank=True)
    punc_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='punc_emp_id')

    def __str__(self):
        return str(self.punc_date)


class PayHistory(models.Model):
    pay_hist_id = models.AutoField(primary_key=True)
    pay_hist_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='pay_hist_emp_id')
    pay_hist_date = models.DateField()
    pay_hist_tot_price = models.BigIntegerField()
    pay_hist_default_price = models.BigIntegerField()
    pay_hist_etc_price = models.BigIntegerField()
    pay_hist_bouns_price = models.BigIntegerField()

    class Meta:
        unique_together = (('pay_hist_emp_id', 'pay_hist_date'),)

    def __str__(self):
        return 'Pay History : {} {}'.format(self.pay_hist_emp_id, self.pay_hist_date)