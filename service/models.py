from django.db import models
from hr.models import Employee
from sales.models import Contract
from client.models import Customer, Company


# Create your models here.
class ServiceType(models.Model):
    srv_type_id = models.AutoField(primary_key=True)
    srv_type_name = models.CharField(max_length=30)
    srv_type_comt = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.srv_type_name)


class ServiceReport(models.Model):
    serviceTypeChoices = (
        ('교육', '교육'),
        ('마이그레이션', '마이그레이션'),
        ('모니터링', '모니터링'),
        ('미팅&회의', '미팅&회의'),
        ('백업&복구', '백업&복구'),
        ('프로젝트상주', '프로젝트상주'),
        ('상주', '상주'),
        ('설치&패치', '설치&패치'),
        ('원격지원', '원격지원'),
        ('일반작업지원', '일반작업지원'),
        ('장애지원', '장애지원'),
        ('정기점검', '정기점검'),
        ('튜닝', '튜닝'),
        ('프로젝트', '프로젝트'),
        ('프리세일즈', '프리세일즈'),
    )
    serviceLocationChoices = (('서울', '서울'), ('경기', '경기'), ('기타', '기타'))
    statusChoices = (('Y', 'Y'), ('N', 'N'))

    srv_id = models.AutoField(primary_key=True)
    srv_date = models.DateField()
    srv_start_datetime = models.DateTimeField()
    srv_end_datetime = models.DateTimeField()
    srv_finish_date_time = models.DateTimeField()
    srv_location = models.CharField(max_length=10, choices=serviceLocationChoices, default='서울')
    srv_directgo = models.CharField(max_length=1, choices=statusChoices, default='N')
    srv_title = models.CharField(max_length=200, help_text="제목을 작성해 주세요.")
    srv_det = models.TextField(help_text="상세 내용을 작성해 주세요.")
    srv_signpath = models.CharField(max_length=254, default='/media/images/signature/nosign.jpg')
    srv_stat = models.CharField(max_length=1, default='N')
    srv_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='srv_emp_id')
    srv_com_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='srv_com_id')
    srv_cust_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='srv_cust_id')
    srv_srvtype_id = models.ForeignKey(ServiceType, on_delete=models.PROTECT, related_name='srv_srvtype_id')
    srv_cont_id = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True, blank=True, related_name='srv_cont_id')

    def __str__(self):
        return 'ServiceReport : {} {}'.format(self.srv_id, self.srv_title)


class ServiceSupportTime(models.Model):
    srv_suptime_id = models.AutoField(primary_key=True)
    srv_suptime_srv_id = models.ForeignKey(ServiceReport, unique=True, on_delete=models.CASCADE, related_name='srv_suptime_srv_id')
    srv_suptime_toth = models.FloatField()
    srv_suptime_hour = models.FloatField()
    srv_suptime_ovh = models.FloatField()
    srv_suptime_price = models.BigIntegerField(default=0)
    srv_suptime_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='srv_suptime_emp_id', null=True)
    srv_suptime_pay_date = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='srv_suptime_pay_date', null=True)

    def __str__(self):
        return str(self.srv_suptime_srv_id)


class OvertimeDaysManage(models.Model):
    ovt_id = models.AutoField(primary_key=True)
    ovt_date = models.DateField(null=True)
    ovt_start_time = models.TimeField()
    ovt_end_time = models.TimeField()
    ovt_type = models.CharField(max_length=2)
    ovt_comt = models.CharField(max_length=200)

    def __str__(self):
        return 'OvertimeDaysManage : {} {}'.format(self.ovt_date, self.ovt_comt)


class ServiceOvertimeDetail(models.Model):
    ovt_det_id = models.AutoField(primary_key=True)
    ovt_det_srv_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='ovt_det_srv_id')
    ovt_det_ovt_id = models.ForeignKey(OvertimeDaysManage, on_delete=models.CASCADE, related_name='ovt_det_ovt_id')
    ovt_det_comt = models.CharField(max_length=200, null=True)

    class Meta:
        unique_together = (('ovt_det_srv_id', 'ovt_det_ovt_id'),)

    def __str__(self):
        return str(self.ovt_det_comt)


class ServiceWorker(models.Model):
    worker_id = models.AutoField(primary_key=True)
    worker_srv_id = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True, blank=True, related_name='worker_srv_id')
    worker_emp_id = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='worker_emp_id')
    worker_emp_name = models.CharField(max_length=30)

    class Meta:
        unique_together = (('worker_srv_id', 'worker_emp_id'),)

    def __str__(self):
        return 'SrviceWorker : {} {}'.format(self.worker_srv_id, self.worker_emp_name)


class ServiceForm(models.Model):
    serviceTypeChoices = (
        ('교육', '교육'),
        ('마이그레이션', '마이그레이션'),
        ('모니터링', '모니터링'),
        ('미팅&회의', '미팅&회의'),
        ('백업&복구', '백업&복구'),
        ('프로젝트상주', '프로젝트상주'),
        ('상주', '상주'),
        ('설치&패치', '설치&패치'),
        ('원격지원', '원격지원'),
        ('일반작업지원', '일반작업지원'),
        ('장애지원', '장애지원'),
        ('정기점검', '정기점검'),
        ('튜닝', '튜닝'),
        ('프로젝트', '프로젝트'),
        ('프리세일즈', '프리세일즈'),
    )
    serviceLocationChoices = (('서울', '서울'), ('경기', '경기'), ('기타', '기타'))
    statusChoices = (('N', 'N'), ('B', 'B'), ('S', 'S'), ('E', 'E'), ('Y', 'Y'))

    srv_form_id = models.AutoField(primary_key=True)
    srv_form_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='srv_form_emp_id')
    srv_form_com_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='srv_form_com_id')
    srv_form_srvtype_id = models.ForeignKey(ServiceType, on_delete=models.PROTECT, related_name='srv_form_srvtype_id')
    srv_form_start_datetime = models.DateTimeField()
    srv_form_end_datetime = models.DateTimeField()
    srv_form_location = models.CharField(max_length=10, choices=serviceLocationChoices, default='서울')
    srv_form_directgo = models.CharField(max_length=1, choices=statusChoices, default='N')
    srv_form_title = models.CharField(max_length=200, help_text="제목을 작성해 주세요.")
    srv_form_det = models.TextField(help_text="상세 내용을 작성해 주세요.")

    def __str__(self):
        return 'ServiceForm : {} {}'.format(self.srv_form_emp_id, self.srv_form_com_id)


class Vacation(models.Model):
    vac_id = models.AutoField(primary_key=True)
    vac_emp_id = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='vac_emp_id')
    vac_date = models.DateField()
    vac_usetype = models.CharField(max_length=2)
    vac_applytype = models.CharField(max_length=2)
    vac_type = models.CharField(max_length=2)

    class Meta:
        unique_together = (('vac_emp_id', 'vac_date'),)

    def __str__(self):
        return 'Vacation : {} {}'.format(self.vac_emp_id,self.vac_date)
