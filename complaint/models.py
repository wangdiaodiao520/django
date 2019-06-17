from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    '''用户表'''
    user_name = models.CharField(max_length=128,unique=True)
    user_password = models.CharField(max_length=256)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'user_form'


class UserForm(forms.Form):
    user_name = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class Complaint(models.Model):
    id = models.AutoField(primary_key=True)
    ts_id = models.CharField(max_length=255)
    cj = models.CharField(max_length=255)
    cx = models.CharField(max_length=255)
    nk = models.CharField(max_length=255)
    js = models.CharField(max_length=255)
    wt = models.CharField(max_length=255)
    time = models.DateField()
    ms = models.TextField()

    class Meta:
        db_table = 'Complaint'