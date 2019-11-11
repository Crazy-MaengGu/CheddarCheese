from django.db import models

# Create your models here.


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
    srv_details = models.TextField(help_text="상세 내용을 작성해 주세요.")
    srv_signpath = models.CharField(max_length=254, default='/media/images/signature/nosign.jpg')
    srv_stat = models.CharField(max_length=1, default='N')
    srv_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='srv_emp_id')
    srv_com_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='srv_com_id')
    srv_cust_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='srv_cust_id')
    srv_type_id = models.ForeignKey(SrviceType, on_delete=models.SET_NULL, related_name='srv_type_id')
    srv_cont_id = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True, blank=True, related_name='srv_cont_id')

    def __str__(self):
        return 'ServiceReport : {} {}'.format(self.srv_id, self.srv_title)


class ServiceSupportTime(models.Model):
    srv_id = models.ForeignKey(ServiceReport, on_delete=models.CASCADE, related_name='srv_id', primary_key=True)
    srv_suptime_totalhour = models.FloatField()
    srv_suptime_hour = models.FloatField()
    srv_suptime_overhour = models.FloatField()
    srv_suptime_price = models.IntegerField(null=True)
    srv_suptime_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='srv_suptime_emp_id', null=True)
    srv_suptime_pay_date = models.DateField(null=True)

    def __str__(self):
        return str(self.srv_type_name)


class OvertimeDaysManage(models.Model):
    overtime_id = models.AutoField(primary_key=True)
    overtime_date = models.DateField(null=True)
    overtime_start_time = models.TimeField()
    overtime_end_time = models.TimeField()
    overtime_type = models.CharField(max_length=2)
    overtime_comt = models.CharField(max_length=200)

    def __str__(self):
        return 'OvertimeDaysManage : {} {}'.format(self.overtime_date, self.overtime_comt)


class ServiceOvertimeDetail(models.Model):
    overtime_detail_srv_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='overtime_detail_srv_id', primary_key=True)
    overtime_detail_id = models.ForeignKey(OvertimeDaysManage, on_delete=models.CASCADE, related_name='overtime_detail_id', primary_key=True)
    overtime_detail_comt = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.overtime_detail_comt)


class ServiceType(models.Model):
    srv_type_id = models.AutoField(primary_key=True)
    srv_type_name = models.CharField(max_length=30)
    srv_type_comt = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.srv_type_name)


class ServiceWorker(models.Model):
    worker_srv_id = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True, blank=True, related_name='srv_cont_id', primary_key=True)
    worker_emp_id = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='srv_cont_id', primary_key=True)
    worker_emp_name = models.CharField(max_length=30)

    def __str__(self):
        return 'SrviceWorker : {} {}'.format(self.worker_srv_id, self.worker_emp_name)


class Vacation(models.Model):
    vac_emp_id = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='vac_emp_id', primary_key=True)
    vac_date = models.DateField(primary_key=True)
    vac_usetype = models.CharField(max_length=2)
    vac_applytype = models.CharField(max_length=2)
    vac_type = models.CharField(max_length=2)

    def __str__(self):
        return 'Vacation : {} {}'.format(self.vac_emp_id,self.vac_date)
