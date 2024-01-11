from django.shortcuts import render, redirect
from django.http import HttpResponse
from UserHandling.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from UserHandling.models import UserData, UserType
from django.contrib.auth.models import User


def login_screen(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_screen(request):
    logout(request)
    return redirect('/log-in')


def signup_screen(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            new_user_data = UserData.objects.create(
                user=User.objects.get(username=form.cleaned_data["username"]),
                user_type=UserType.objects.get(type_name=form.cleaned_data["user_type"])
            )
            return redirect('/log-in')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
