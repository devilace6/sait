from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .forms import UserRegistrationForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from .forms import UserLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/registration.html', {'user_form': user_form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
          user = form.get_user()
          login(request, user)
          messages.success(request, 'Вы успешно вошли')
          return redirect('home')
    else:
        form = UserLoginForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'registration/login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect('login')