from django.conf.urls import url
from . import views

app_name = 'dashboard'

urlpatterns = [
    url(r'^service/$', views.dashboard_service, name='dashboardservice'),
    # url(r'^overhour/$', views.over_hour, name='over_hour'),
    # url(r'^overjson/$', views.over_asjson, name='over_ajax_url'),
]
