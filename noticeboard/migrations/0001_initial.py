# Generated by Django 2.2.7 on 2019-11-13 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
        ('hr', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('board_id', models.AutoField(primary_key=True, serialize=False)),
                ('board_title', models.CharField(help_text='제목을 작성해 주세요.', max_length=200)),
                ('board_det', models.TextField(help_text='상세 내용을 작성해 주세요.')),
                ('board_type', models.CharField(max_length=2)),
                ('board_files', models.FileField(blank=True, null=True, upload_to='board/%Y_%m')),
                ('board_write_date_time', models.DateTimeField()),
                ('board_edit_date_time', models.DateTimeField()),
                ('board_com_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='board_com_id', to='client.Company')),
                ('board_srv_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='board_srv_id', to='service.ServiceReport')),
                ('board_writer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_writer_id', to='hr.Employee')),
            ],
        ),
    ]