from django.db import models
from hr.models import Employee

# Create your models here.


class Company(models.Model):
    statusChoices = (('Y', 'Y'), ('N', 'N'), ('X', 'X'))

    com_id = models.AutoField(primary_key=True)
    com_name = models.CharField(max_length=200, unique=True)
    com_name_ko = models.CharField(max_length=200, unique=True)
    com_num = models.CharField(max_length=30, null=True, blank=True)
    com_addr = models.CharField(max_length=200, null=True)
    com_latitude = models.FloatField(null=True, blank=True)
    com_longitude = models.FloatField(null=True, blank=True)
    com_stat = models.CharField(max_length=1, choices=statusChoices, default='Y')

    def __str__(self):
        return self.com_name


class Customer(models.Model):
    statusChoices = (('Y', 'Y'), ('N', 'N'))

    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=30)
    cust_dept_name = models.CharField(max_length=30, null=True, blank=True)
    cust_phone = models.CharField(max_length=20, null=True, blank=True)
    cust_email = models.CharField(max_length=254, null=True, blank=True)
    cust_stat = models.CharField(max_length=1, choices=statusChoices, default='Y')
    cust_com_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='cust_com_id')

    def __str__(self):
        return self.cust_name


class SupportHistory(models.Model):
    sup_hist_id = models.AutoField(primary_key=True)
    sup_hist_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='sup_hist_emp_id')
    sup_hist_com_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='sup_hist_com_id')
    sup_hist_type = models.CharField(max_length=2)
    sup_hist_start_date = models.DateField()
    sup_hist_end_date = models.DateField()

    class Meta:
        unique_together = (('sup_hist_emp_id', 'sup_hist_com_id', 'sup_hist_type'),)

    def __str__(self):
        return 'Company Sup Hist : {} {} {}'.format(self.sup_hist_com_id, self.sup_hist_type, self.sup_hist_start_date)


class CompanyInfo(models.Model):
    com_info_id = models.AutoField(primary_key=True)
    com_info_com_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='com_info_com_id')
    com_info_seq = models.SmallIntegerField()
    com_info_attribute = models.CharField(max_length=30)
    com_info_attribute_comt = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = (('com_info_com_id', 'com_info_seq'),)

    def __str__(self):
        return self.com_info_attribute


class CompanyInfoDetail(models.Model):
    com_info_det_id = models.AutoField(primary_key=True)
    com_info_det_com_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='com_info_det_com_id')
    com_info_det_com_info_id = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, related_name='com_info_det_com_info_id')
    com_info_det_seq = models.SmallIntegerField()
    com_info_det_comt = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        unique_together = (('com_info_det_com_id', 'com_info_det_com_info_id', 'com_info_det_seq'),)

    def __str__(self):
        return self.com_info_det_comt