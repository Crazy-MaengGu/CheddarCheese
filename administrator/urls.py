from django.urls import path
from . import views

urlpatterns = [
    path('administrator/', views.useradd, name='useradd'),
]
