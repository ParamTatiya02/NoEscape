from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import  CreateUserForm


def home(request):
    return render(request, '../templates/NoEscape/home.html')


def main(request):
    return render(request, '../templates/NoEscape/main.html')



def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../../main/profile/')
        else:
            messages.info(request, 'Username or Password is Incorrect')

    context = {}
    return render(request, '../templates/NoEscape/login.html', context)


def sign_up(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, '../templates/NoEscape/sign_up.html', context)


def contact(request):
    return render(request, '../templates/NoEscape/contact.html')


def about(request):
    return render(request, '../templates/NoEscape/about.html')
