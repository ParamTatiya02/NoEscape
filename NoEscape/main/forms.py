from .models import Video, Applicant
from django import forms


class Video_form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ("name", "phone", "email", "video")


class Complaint(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ("name", "phone", "email", "complaint")
