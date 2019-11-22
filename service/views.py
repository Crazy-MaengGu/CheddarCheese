from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .functions import *
from .models import ServiceForm
# Create your views here.

@login_required
def day_report(request, day=None):
    if day is None:
        day = str(datetime.datetime.today())[:10]
    Date = datetime.datetime(int(day[:4]), int(day[5:7]), int(day[8:10]))
    beforeDate = Date - datetime.timedelta(days=1)
    afterDate = Date + datetime.timedelta(days=1)

    solution = dayreport_query2(empDeptName="솔루션지원팀", day=day)
    db = dayreport_query2(empDeptName="DB지원팀", day=day)
    sales1 = dayreport_query2(empDeptName="영업1팀", day=day)
    sales2 = dayreport_query2(empDeptName="영업2팀", day=day)
    infra = dayreport_query2(empDeptName="인프라서비스사업팀", day=day)

    dept = request.user.employee.empDeptName

    rows = []
    if dept == '영업2팀':
        rows.append([
            {'title': '영업2팀', 'service': sales2[0], 'education': sales2[1], 'vacation': sales2[2]},
            {'title': '영업1팀', 'service': sales1[0], 'education': sales1[1], 'vacation': sales1[2]},
        ])
        rows.append([
            {'title': '솔루션지원팀', 'service': solution[0], 'education': solution[1], 'vacation': solution[2]},
            {'title': 'DB지원팀', 'service': db[0], 'education': db[1], 'vacation': db[2]},
        ])
        rows.append([
            {'title': '인프라서비스사업팀', 'service': infra[0], 'education': infra[1], 'vacation': infra[2]},
            {'title': '', 'service': '', 'education': '', 'vacation': ''},
        ])
    elif dept == '솔루션지원팀':
        rows.append([
            {'title': '솔루션지원팀', 'service': solution[0], 'education': solution[1], 'vacation': solution[2]},
            {'title': 'DB지원팀', 'service': db[0], 'education': db[1], 'vacation': db[2]},
        ])
        rows.append([
            {'title': '영업1팀', 'service': sales1[0], 'education': sales1[1], 'vacation': sales1[2]},
            {'title': '영업2팀', 'service': sales2[0], 'education': sales2[1], 'vacation': sales2[2]},
        ])
        rows.append([
            {'title': '인프라서비스사업팀', 'service': infra[0], 'education': infra[1], 'vacation': infra[2]},
            {'title': '', 'service': '', 'education': '', 'vacation': ''},
        ])
    elif dept == 'DB지원팀':
        rows.append([
            {'title': 'DB지원팀', 'service': db[0], 'education': db[1], 'vacation': db[2]},
            {'title': '솔루션지원팀', 'service': solution[0], 'education': solution[1], 'vacation': solution[2]},
        ])
        rows.append([
            {'title': '영업1팀', 'service': sales1[0], 'education': sales1[1], 'vacation': sales1[2]},
            {'title': '영업2팀', 'service': sales2[0], 'education': sales2[1], 'vacation': sales2[2]},
        ])
        rows.append([
            {'title': '인프라서비스사업팀', 'service': infra[0], 'education': infra[1], 'vacation': infra[2]},
            {'title': '', 'service': '', 'education': '', 'vacation': ''},
        ])
    elif dept == '인프라서비스사업팀':
        rows.append([
            {'title': '인프라서비스사업팀', 'service': infra[0], 'education': infra[1], 'vacation': infra[2]},
            {'title': '', 'service': '', 'education': '', 'vacation': ''},
        ])
        rows.append([
            {'title': '영업1팀', 'service': sales1[0], 'education': sales1[1], 'vacation': sales1[2]},
            {'title': '영업2팀', 'service': sales2[0], 'education': sales2[1], 'vacation': sales2[2]},
        ])
        rows.append([
            {'title': '솔루션지원팀', 'service': solution[0], 'education': solution[1], 'vacation': solution[2]},
            {'title': 'DB지원팀', 'service': db[0], 'education': db[1], 'vacation': db[2]},
        ])
    else:
        rows.append([
            {'title': '영업1팀', 'service': sales1[0], 'education': sales1[1], 'vacation': sales1[2]},
            {'title': '영업2팀', 'service': sales2[0], 'education': sales2[1], 'vacation': sales2[2]},
        ])
        rows.append([
            {'title': '솔루션지원팀', 'service': solution[0], 'education': solution[1], 'vacation': solution[2]},
            {'title': 'DB지원팀', 'service': db[0], 'education': db[1], 'vacation': db[2]},
        ])
        rows.append([
            {'title': '인프라서비스사업팀', 'service': infra[0], 'education': infra[1], 'vacation': infra[2]},
            {'title': '', 'service': '', 'education': '', 'vacation': ''},
        ])

    context = {
        'day': day,
        'Date': Date,
        'beforeDate': beforeDate,
        'afterDate': afterDate,
        'rows': rows,
    }

    return render(request, 'service/dayreport.html', context)