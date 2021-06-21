from django.db import models


class Applicant(models.Model):
    name = models.CharField(max_length=100, default='add name')
    phone = models.IntegerField(default='add number')
    email = models.EmailField(default='abc@edf.com')
    complaint = models.CharField(max_length=200, default='add address')

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=100, default='add name')
    phone = models.IntegerField(default='add number')
    email = models.EmailField(default='abc@edf.com')
    video = models.FileField(upload_to='videos/', null=True)

    def __str__(self):
        return self.name
