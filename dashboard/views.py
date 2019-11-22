from django.shortcuts import render

# Create your views here.

from datetime import datetime, timedelta
import json

from django.contrib.auth.decorators import login_required
from django.db.models import Q, F, Case, When, Value, CharField
from django.db.models import Sum, Count
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from service.functions import dayreport_query2
from hr.models import Employee
from django.db.models import functions
from django.db.models.functions import Coalesce



@login_required
def dashboard_service(request):
    template = loader.get_template('dashboard/dashboardservice.html')

    return str('hi')
