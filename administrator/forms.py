from django import forms
from django.contrib.auth.models import User

class UseraddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

        widgets = {
            'userName': forms.TextInput(attrs={'class': 'form-control', 'id': 'userName'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'id': 'password'}),
            'confirmPassword': forms.TextInput(attrs={'class': 'form-control', 'id': 'confirmPassword'}),
            'firstName': forms.TextInput(attrs={'class': 'form-control', 'id': 'firstName'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control', 'id': 'lastName'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email'}),
        }

        labels = {
            'userName': '아이디',
            'password': '비밀번호',
            'confirmPassword': '비밀번호 재확인',
            'firstName': '성',
            'lastName': '이름',
            'email': '이메일',
        }
