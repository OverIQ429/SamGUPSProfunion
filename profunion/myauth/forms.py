from django import forms
from .models import Profile, Appends, AllGroups, News, Photo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']

class NewForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ['created_at']
        fields = ['type', 'name', 'article', 'avatar', 'document']
        widgets = {'type': forms.CheckboxInput(),
            'created_at': forms.DateTimeInput(attrs={'readonly': 'readonly'}),}
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
    email = forms.EmailField(label='Почта',required=True)
    phone_number = forms.CharField(label='Телефон',required=False)
    group = forms.ModelChoiceField(label='Группа',queryset=AllGroups.objects.all(), required=False)
    name = forms.CharField(label='Имя',required=False)
    lastname = forms.CharField(label='Фамилия',required=False)
    secondname = forms.CharField(label='Отчество',required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('name','lastname','secondname','email', 'phone_number','group',)

class ReportUsersFilterForm(forms.Form):
    faculty = forms.CharField(label='Факультет', max_length=100)
    group = forms.CharField(label='Группа', max_length=100)
    course = forms.IntegerField(label='Курс')
    date_from = forms.DateField(label='Дата с')
    date_to = forms.DateField(label='Дата по')