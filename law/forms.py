from django import forms
from django.forms.widgets import EmailInput, HiddenInput, TextInput ,Textarea
from .models import IletisimModel


class IletisimModelForm(forms.ModelForm):
   
    class Meta:
        model = IletisimModel
        exclude = ('created_date','okundu_mu')
        widgets = {
            "isim" : TextInput(attrs={"class":"form-control"}),
            "email" : EmailInput(attrs={"type":"email","class":"form-control"}),
            "subject" : TextInput(attrs={"class":"form-control"}),
            "message" : Textarea(attrs={"class":"form-control"}),       
          
        }