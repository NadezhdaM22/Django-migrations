from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


#class UserRegForm(forms.Form):
class UserRegForm(UserCreationForm):
    email=forms.EmailField(
        label="Введите email",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'})
    )
    username=forms.CharField(
        label="Введите логин",
        required=True,
        help_text='Нельзя вводить символы @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'})
    )

    #some = forms.ModelChoiceField(queryset=User.objects.all())
    password1=forms.CharField(
        label="Введите пароль",
        required=True,
        help_text="Введите смешной пароль",
        widget=forms.PasswordInput(attrs={'class' : 'form-control'})
    )
    password2=forms.CharField(
        label="Подтвердите пароль",
        required=True,
        widget=forms.PasswordInput(attrs={'class' : 'form-control'})
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', ]



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label="Введите email",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'})
    )
    username = forms.CharField(
        label="Введите логин",
        required=True,
        help_text='Нельзя вводить символы @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'})
    )

    class Meta:
        model = User
        fields = ['username', 'email' ]


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label="Загрузить фото",
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img' ]

