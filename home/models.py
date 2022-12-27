from django.contrib.auth.models import User
from django.db import models
from django import forms


class activity(models.Model):
    name = models.CharField(max_length=100);
    title = models.CharField(max_length=20);
    img = models.ImageField(blank=True, upload_to='images/')


class comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    title = models.CharField(max_length=40)
    comment = models.CharField(max_length=400)

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['name', 'comment']
    class Meta:
        db_table = ['my_table_name']
        fields = ['name', 'comment']

class message(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    title = models.CharField(max_length=40)
    message = models.CharField(max_length=400)