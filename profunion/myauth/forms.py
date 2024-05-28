from django import forms
from .models import Profile, Appends, AllGroups
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    group = forms.ChoiceField(choices=[('1', 'Группа 1'), ('group2', 'Группа 2')], required=False)
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("avatar", )

class AppendsForm(forms.ModelForm):
    class Meta:
        model = Appends
        fields = ("file", )

class AppendsEditForm(forms.ModelForm):
    class Meta:
        model = Appends
        fields = ("file",'commentary','decision',)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)
    group = forms.ModelChoiceField(queryset=AllGroups.objects.all(), required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number','group',)

class ReportUsersFilterForm(forms.Form):
    faculty = forms.CharField(label='Факультет', max_length=100)
    group = forms.CharField(label='Группа', max_length=100)
    course = forms.IntegerField(label='Курс')
    date_from = forms.DateField(label='Дата с')
    date_to = forms.DateField(label='Дата по')