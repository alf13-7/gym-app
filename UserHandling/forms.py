from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


user_type_choices = (
    ("PT", "Personal Trainer"),
    ("Standard", "Standard User")
)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=user_type_choices)

    class Meta:
        model = User
        fields = ['username', 'user_type', 'password1', 'password2']
