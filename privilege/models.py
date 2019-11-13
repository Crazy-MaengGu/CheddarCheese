from django.db import models
from hr.models import Employee, Department

# Create your models here.


class PrivilegeDetail(models.Model):
    priv_det_id = models.AutoField(primary_key=True)
    priv_det_date = models.DateField()
    priv_det_level_type = models.CharField(max_length=2)
    priv_det_comt = models.CharField(max_length=200, null=True)

    def __str__(self):
        return 'Privilege : {} {} {}'.format(self.priv_det_id, self.priv_det_level_type, self.priv_det_comt)


class PrivilegeRole(models.Model):
    priv_role_id = models.AutoField(primary_key=True)
    priv_role_seq = models.IntegerField()
    priv_role_det_id = models.ForeignKey(PrivilegeDetail, on_delete=models.CASCADE, related_name='priv_role_det_id')
    priv_role_comt = models.CharField(max_length=200, null=True)

    class Meta:
        unique_together = (('priv_role_seq', 'priv_role_det_id'),)

    def __str__(self):
        return 'Role : {} {} {}'.format(self.priv_role_seq, self.priv_role_det_id, self.priv_role_comt)


class PrivilegeGrant(models.Model):
    priv_grant_id = models.AutoField(primary_key=True)
    priv_grant_role_id = models.ForeignKey(PrivilegeRole, on_delete=models.CASCADE, related_name='priv_grant_role_id', null=True)
    priv_grant_det_id = models.ForeignKey(PrivilegeDetail, on_delete=models.CASCADE, related_name='priv_grant_det_id')
    priv_grant_dept_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='priv_grant_dept_id', null=True)
    priv_grant_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='priv_grant_emp_id', null=True)

    def __str__(self):
        return 'Privilege Grant : {} {} {}'.format(self.priv_grant_id, self.priv_grant_dept_id, self.priv_grant_emp_id)