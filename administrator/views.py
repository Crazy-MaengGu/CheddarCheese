from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.

def useradd(request):
    return render(request, 'administrator/usermanage.html')
