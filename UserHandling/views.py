from django.shortcuts import render, redirect
from django.http import HttpResponse
from UserHandling.forms import LoginForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout


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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/log-in')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
