import datetime
import json

from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import UseraddForm

# Create your views here.

def userselect(request):
    user = User.objects.all()
    #user = User.objects.filter(published_date__lte=timezone.now()).order_by('id')
    return render(request, 'administrator/usermanage.html')


def user_asjson(request):
    userId = request.POST['userId']
    userName = request.POST['userName']
    lastLogin = request.POST['lastLogin']
    startDate = request.POST['startDate']
    endDate = request.POST['endDate']

    Users = User.objects.all()
    if startDate:
        Users = Users.filter(boardWriteDatetime__gte=last_login)
    if endDate:
        Users = Users.filter(boardWriteDatetime__lte=last_login)
    if userName:
        Users = Users.filter(boardWriter__empName__icontains=empName)

    Users = Users.values('boardWriteDatetime', 'serviceId__serviceType', 'boardWriter__empName', 'serviceId__companyName', 'boardTitle', 'boardDetails', 'boardId')
    structure = json.dumps(list(Users), cls=DjangoJSONEncoder)
    return HttpResponse(structure, content_type='application/json')


@login_required
def showusers(request):
    if request.method == "POST":
        userId = request.POST['userId']
        userName = request.POST['userName']
        lastLogin = request.POST['lastLogin']
        startDate = request.POST['startDate']
        endDate = request.POST['endDate']

        context = {
            'filter': 'Y',
            'userId': userId,
            'userName': userName,
            'lastLogin': lastLogin,
            'startDate': startDate,
            'endDate': endDate,

        }
        return render(request, 'administrator/showuserss.html', context)

    else:
        context = {
            'filter': 'N',
        }
        return render(request, 'administrator/showuserss.html', context)
