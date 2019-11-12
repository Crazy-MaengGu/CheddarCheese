from django.db import models
from hr.models import Employee
from service.models import ServiceReport
from client.models import Company

# Create your models here.

class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    board_title = models.CharField(max_length=200, help_text="제목을 작성해 주세요.")
    board_det = models.TextField(help_text="상세 내용을 작성해 주세요.")
    board_type = models.CharField(max_length=2)
    board_files = models.FileField(null=True, blank=True, upload_to="board/%Y_%m")
    board_write_date_time = models.DateTimeField()
    board_edit_date_time = models.DateTimeField()
    board_writer_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='board_writer_id')
    board_srv_id = models.ForeignKey(ServiceReport, on_delete=models.SET_NULL, related_name='board_srv_id', null=True, blank=True)
    board_com_id = models.ForeignKey(Company, on_delete=models.SET_NULL, related_name='board_com_id', null=True)

    def __str__(self):
        return 'Board : {} {}'.format(self.board_writer_id, self.board_title)