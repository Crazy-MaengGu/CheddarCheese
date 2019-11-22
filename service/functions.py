import datetime
import os
import math
import re
from io import BytesIO
import json

from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import QueryDict
from .models import ServiceReport, Vacation


def dayreport_query2(empDeptName, day):
    Date = datetime.datetime(int(day[:4]), int(day[5:7]), int(day[8:10]))
    Date_min = datetime.datetime.combine(Date, datetime.datetime.min.time())
    Date_max = datetime.datetime.combine(Date, datetime.datetime.max.time())
    if datetime.datetime.weekday(Date) >= 5 or Eventday.objects.filter(Q(eventDate=Date) & Q(eventType='휴일')):
        holiday = True
    else:
        holiday = False

    serviceDept = ServiceReport.objects.filter(
        Q(empDeptName=empDeptName) & (Q(serviceBeginDatetime__lte=Date_max) & Q(serviceFinishDatetime__gte=Date_min))
    ).order_by('serviceBeginDatetime')

    vacationDept = Vacation.objects.filter(
        Q(empDeptName=empDeptName) & Q(vacationDate=Date)
    )

    inDept = User.objects.filter(
        Q(employee__empDeptName=empDeptName) & Q(employee__empStatus='Y')
    ).exclude(
        Q(employee__empId__in=serviceDept.values('empId')) | Q(employee__empId__in=vacationDept.values('empId'))
    )

    listService = []
    listEducation = []
    listVacation = []

    for service in serviceDept:
        if service.serviceType == '상주' or service.serviceType == '프로젝트상주':
            flag = '상주'
        elif service.directgo == 'Y':
            flag = '직출'
        else:
            flag = ''

        if service.serviceType == '교육':
            listEducation.append({
                'serviceId': service.serviceId,
                'flag': flag,
                'empName': service.empName,
                'serviceBeginDatetime': service.serviceBeginDatetime,
                'serviceFinishDatetime': service.serviceFinishDatetime,
                'serviceStatus': service.serviceStatus,
                'serviceTitle': service.serviceTitle,
                'sortKey': service.empId.empRank,
            })
        else:
            listService.append({
                'serviceId': service.serviceId,
                'flag': flag,
                'empName': service.empName,
                'serviceBeginDatetime': service.serviceBeginDatetime,
                'serviceFinishDatetime': service.serviceFinishDatetime,
                'serviceStatus': service.serviceStatus,
                'companyName': service.companyName,
                'serviceType': service.serviceType,
                'serviceTitle': service.serviceTitle,
                'sortKey': service.empId.empRank,
            })

    if not holiday:
        for emp in inDept:
            listService.append({
                'serviceId': '',
                'flag': '',
                'empName': emp.employee.empName,
                'serviceBeginDatetime': datetime.datetime(int(day[:4]), int(day[5:7]), int(day[8:10]), 9, 0),
                'serviceFinishDatetime': datetime.datetime(int(day[:4]), int(day[5:7]), int(day[8:10]), 18, 0),
                'serviceStatus': '',
                'companyName': emp.employee.dispatchCompany,
                'serviceType': '',
                'serviceTitle': emp.employee.message,
                'sortKey': emp.employee.empRank,
            })

        for vacation in vacationDept:
            listVacation.append({
                'empName': vacation.empName,
                'serviceBeginDatetime': Date,
                'vacationType': vacation.vacationType[:2],
                'sortKey': vacation.empId.empRank,
            })

            if vacation.vacationType != '일차' and vacation.empId.empId not in serviceDept.values_list('empId', flat=True):
                if vacation.empId.dispatchCompany == '내근':
                    flag = ''
                else:
                    flag = '상주'

                if vacation.vacationType == '오전반차':
                    startDateTime = datetime.datetime(int(day[:4]), int(day[5:7]), int(day[8:10]), 14, 0)
                    endDateTime = datetime.datetime(int(day[:4]), int(day[5:7]), int(day[8:10]), 18, 0)
                elif vacation.vacationType == '오후반차':
                    startDateTime = datetime.datetime(int(day[:4]), int(day[5:7]), int(day[8:10]), 9, 0)
                    endDateTime = datetime.datetime(int(day[:4]), int(day[5:7]), int(day[8:10]), 14, 0)

                listService.append({
                    'serviceId': '',
                    'flag': flag,
                    'empName': vacation.empName,
                    'serviceBeginDatetime': startDateTime,
                    'serviceFinishDatetime': endDateTime,
                    'serviceStatus': '',
                    'companyName': vacation.empId.dispatchCompany,
                    'serviceType': '',
                    'serviceTitle': vacation.empId.message,
                    'sortKey': vacation.empId.empRank,
                })

    listService.sort(key=lambda x: x['sortKey'])
    listEducation.sort(key=lambda x: x['sortKey'])
    listVacation.sort(key=lambda x: x['sortKey'])

    queryService = []
    queryEducation = []
    queryVacation = []

    for l in listService:
        temp = QueryDict('', mutable=True)
        temp.update(l)
        queryService.append(temp)
    for l in listEducation:
        temp = QueryDict('', mutable=True)
        temp.update(l)
        queryEducation.append(temp)
    for l in listVacation:
        temp = QueryDict('', mutable=True)
        temp.update(l)
        queryVacation.append(temp)

    return queryService, queryEducation, queryVacation
