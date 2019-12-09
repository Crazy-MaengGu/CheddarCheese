from django.urls import path
from . import views

urlpatterns = [
    path('administrator/', views.userselect, name='userselect'),
    path('showusers/', views.showusers, name='showusers'),
    path('administrator/json/', views.user_asjson, name='user_ajax_url'),
]
