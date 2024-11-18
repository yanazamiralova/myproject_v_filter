from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser, Orders
from datetime import date, datetime


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Обязательное поле. Введите действующий email.')

    # patronymic = forms.CharField(verbose_name='Отчество', max_length=120)
    # phone = forms.CharField(verbose_name='Телефон', max_length=12)

    class Meta:
        model = CustomUser
        fields = ('username', 'last_name', 'first_name', 'patronymic', 'email', 'phone', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class NewOrderForm(forms.ModelForm):
    # orderdate = forms.DateField(label='Дата', input_formats='%Y-%m-%d', initial=date.today,
    #                             widget=forms.DateInput(attrs={'type': 'date'}))
    # ordertime = forms.TimeField(label='Время', input_formats='%H:%M', initial=datetime.now().strftime("%H:%M:%S"),
    #                             widget=forms.TimeInput(attrs={'type': 'time'}))
    orderdatetime = forms.DateTimeField(label='Дата и время', input_formats='%Y-%m-%d %H:%M:%S', initial=datetime.now(),
                                        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    # def __init__(self, *args, **kwargs):
    #     self.owner = kwargs.pop('user', None)
    #     print(self.owner)
    #     super(NewOrderForm, self).__init__(*args, **kwargs)
    #
    # def save(self, commit=True):
    #     obj = super(NewOrderForm, self).save(commit=False)
    #     obj.owner = self.owner
    #     if commit:
    #         obj.save()
    #     return obj

    class Meta:
        model = Orders
        fields = ['service', 'payment', 'adress', 'contact_phone',
                  'orderdatetime']  # 'orderdate', 'ordertime' - с ними не работет
