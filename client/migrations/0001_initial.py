# Generated by Django 2.2.7 on 2019-11-13 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('com_id', models.AutoField(primary_key=True, serialize=False)),
                ('com_name', models.CharField(max_length=200, unique=True)),
                ('com_name_ko', models.CharField(max_length=200, unique=True)),
                ('com_num', models.CharField(blank=True, max_length=30, null=True)),
                ('com_addr', models.CharField(max_length=200, null=True)),
                ('com_latitude', models.FloatField(blank=True, null=True)),
                ('com_longitude', models.FloatField(blank=True, null=True)),
                ('com_stat', models.CharField(choices=[('Y', 'Y'), ('N', 'N'), ('X', 'X')], default='Y', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('com_info_id', models.AutoField(primary_key=True, serialize=False)),
                ('com_info_seq', models.SmallIntegerField()),
                ('com_info_attribute', models.CharField(max_length=30)),
                ('com_info_attribute_comt', models.CharField(blank=True, max_length=200, null=True)),
                ('com_info_com_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='com_info_com_id', to='client.Company')),
            ],
            options={
                'unique_together': {('com_info_com_id', 'com_info_seq')},
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=30)),
                ('cust_dept_name', models.CharField(blank=True, max_length=30, null=True)),
                ('cust_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('cust_email', models.CharField(blank=True, max_length=254, null=True)),
                ('cust_stat', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='Y', max_length=1)),
                ('cust_com_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cust_com_id', to='client.Company')),
            ],
        ),
        migrations.CreateModel(
            name='SupportHistory',
            fields=[
                ('sup_hist_id', models.AutoField(primary_key=True, serialize=False)),
                ('sup_hist_type', models.CharField(max_length=2)),
                ('sup_hist_start_date', models.DateField()),
                ('sup_hist_end_date', models.DateField()),
                ('sup_hist_com_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sup_hist_com_id', to='client.Company')),
                ('sup_hist_emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sup_hist_emp_id', to='hr.Employee')),
            ],
            options={
                'unique_together': {('sup_hist_emp_id', 'sup_hist_com_id', 'sup_hist_type')},
            },
        ),
        migrations.CreateModel(
            name='CompanyInfoDetail',
            fields=[
                ('com_info_det_id', models.AutoField(primary_key=True, serialize=False)),
                ('com_info_det_seq', models.SmallIntegerField()),
                ('com_info_det_comt', models.CharField(blank=True, max_length=200, null=True)),
                ('com_info_det_com_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='com_info_det_com_id', to='client.Company')),
                ('com_info_det_com_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='com_info_det_com_info_id', to='client.CompanyInfo')),
            ],
            options={
                'unique_together': {('com_info_det_com_id', 'com_info_det_com_info_id', 'com_info_det_seq')},
            },
        ),
    ]
