from django import forms

from client.models import Company
from .models import ServiceReport, ServiceForm


class ServiceReportForm(forms.ModelForm):
    startdate = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date', "max": '9999-12-31', 'id': 'startdate', 'onchange': "showVal(this.value)"}))
    starttime = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'time', 'id': 'starttime'}))
    enddate = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date', "max": '9999-12-31', 'id': 'enddate'}))
    endtime = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'time', 'id': 'endtime'}))
    coWorkers = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'magicsearch form-control', 'id': 'coWorkers', 'autocomplete': 'off'}))
    contracts = forms.CharField(max_length=300, required=False, widget=forms.TextInput(
        attrs={'class': 'magicsearch form-control', 'id': 'contracts', 'autocomplete': 'off', 'onkeydown': 'magicsearchtab(contracts)'}
    ))

    class Meta:
        model = ServiceReport
        fields = ('contractId', 'companyName', 'serviceType',
                  'startdate', 'starttime', 'enddate', 'endtime',
                  'serviceLocation', 'directgo', 'coWorkers', 'serviceTitle', 'serviceDetails')

        widgets = {
            'companyName': forms.TextInput(attrs={'class': 'form-control magicsearch', 'id': 'companyName', 'autocomplete': 'off', 'onkeydown': 'magicsearchtab(companyName)'}),
            'serviceType': forms.Select(attrs={'class': 'form-control', 'id': "serviceType"}),
            'serviceLocation': forms.Select(attrs={'class': 'form-control', 'id': 'serviceLocation'}),
            'directgo': forms.Select(attrs={'class': 'form-control', 'id': 'directgo'}),
            'serviceTitle': forms.TextInput(attrs={'class': 'form-control', 'id': 'serviceTitle'}),
            'serviceDetails': forms.Textarea(attrs={'class': 'form-control', 'id': 'serviceDetails'}),
        }

    def __init__(self, *args, **kwargs):
        super(ServiceReportForm, self).__init__(*args, **kwargs)
        self.fields["companyName"].queryset = Company.objects.filter(companyStatus='Y').order_by('companyName')


class ServiceReportForm(forms.ModelForm):

    class Meta:
        model = ServiceForm
        fields = ('companyName', 'serviceType',
                  'serviceStartTime', 'serviceEndTime',
                  'serviceLocation', 'directgo', 'serviceTitle', 'serviceDetails')

        widgets = {
            'srv_form_com_id': forms.Select(attrs={'class': 'form-control', 'id': 'srv_form_com_id'}),
            'srv_form_srvtype_id': forms.Select(attrs={'class': 'form-control', 'id': "srv_form_srvtype_id"}),
            'srv_form_start_datetime': forms.TextInput(attrs={'class': 'form-control', 'id': "srv_form_start_datetime", 'type': 'time'}),
            'srv_form_end_datetime': forms.TextInput(attrs={'class': 'form-control', 'id': "srv_form_end_datetime", 'type': 'time'}),
            'srv_form_location': forms.Select(attrs={'class': 'form-control', 'id': 'srv_form_location'}),
            'srv_form_directgo': forms.Select(attrs={'class': 'form-control', 'id': 'srv_form_directgo'}),
            'srv_form_title': forms.TextInput(attrs={'class': 'form-control', 'id': 'srv_form_title'}),
            'srv_form_det': forms.Textarea(attrs={'class': 'form-control', 'id': 'srv_form_det'}),
        }

    def __init__(self, *args, **kwargs):
        super(ServiceReportForm, self).__init__(*args, **kwargs)
        self.fields["companyName"].queryset = Company.objects.filter(companyStatus='Y').order_by('companyName')
