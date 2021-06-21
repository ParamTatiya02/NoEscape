from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Video, Applicant
from .forms import Video_form, Complaint


def home(request):
    return render(request, '../templates/NoEscape/home.html')


def main(request):
    return render(request, '../templates/NoEscape/main.html')


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
