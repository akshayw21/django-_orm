from django import forms
from django.db.models import fields
from .models import Emp,Account,Empqualification

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'

class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields='__all__'


class EmpqualificationForm(forms.ModelForm):
    class Meta:
        model=Empqualification
        fields='__all__'


#---------Auth app----------user form---
from django.contrib.auth.models import User
class UserForm1(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'


class UserForm2(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','user_permissions','password']


from django.contrib.auth.forms import UserCreationForm

class UserForm3(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

from .models import UserInfo,UserInfo2
class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields='__all__'


class UserInfoForm2(UserCreationForm):
    class Meta:
        model=UserInfo2
        fields=['username','first_name','last_name','age','contact','email','gender','password1','password2']


from .models import Singer,Songs

class SingerForm(forms.ModelForm):
    class Meta:
        model=Singer
        fields='__all__'

class SongsForm(forms.ModelForm):
    class Meta:
        model=Songs
        fields='__all__'
