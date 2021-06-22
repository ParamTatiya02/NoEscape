from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Video, Applicant,Camera
from .forms import Video_form, Complaint, CreateUserForm,Camera_form


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
            return redirect('main')
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


def complaint(request):
    form = Applicant()
    if request.method == 'POST':
        form = Complaint(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Complaint Successfully Registered')
            return redirect('../profile')
    context = {'form': form}
    return render(request, '../templates/NoEscape/complaint.html', context)


def about(request):
    return render(request, '../templates/NoEscape/about.html')


def evidence(request):
    all_video = Video.objects.all()
    if request.method == "POST":
        form = Video_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evidence Successfully Uploaded')
            return redirect('main')
    else:
        form = Video_form()
    return render(request, '../templates/NoEscape/evidence.html', {"form": form, "all": all_video})


def camera(request):
    form = Camera()
    if request.method == 'POST':
        form = Camera_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Camera added Successfully')
            return redirect('camera')
    context = {'form': form}
    return render(request, '../templates/NoEscape/camera.html', context)
