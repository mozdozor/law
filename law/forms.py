from ckeditor.fields import RichTextField, RichTextFormField
from django import forms
from django.db.models.fields.files import ImageField
from django.forms.widgets import EmailInput, FileInput, HiddenInput, Select, TextInput ,Textarea
from .models import HakkimizdaModel, IletisimModel,SliderModel


class IletisimModelForm(forms.ModelForm):
   
    class Meta:
        model = IletisimModel
        exclude = ('created_date','okundu_mu')
        widgets = {
            "isim" : TextInput(attrs={"class":"form-control"}),
            "email" : EmailInput(attrs={"type":"email","class":"form-control"}),
            "phone" : TextInput(attrs={"class":"form-control"}),
            "subject" : TextInput(attrs={"class":"form-control"}),
            "message" : Textarea(attrs={"class":"form-control"}),       
          
        }



class SliderModelForm(forms.ModelForm):
    class Meta:
        model = SliderModel
        exclude = ('created_date','updated_date')
        widgets = {
            "main_title" : TextInput(attrs={"class":"form-control"}),
            "top_title" : TextInput(attrs={"class":"form-control"}),
            "bottom_title" : TextInput(attrs={"class":"form-control"}),
            "is_slider" : Select(attrs={"class":"form-control"}),
          
        }





class HakkimizdaModelForm(forms.ModelForm):
    class Meta:
        model = HakkimizdaModel
        exclude = ('created_date','updated_date')
        widgets = {
            "title" : TextInput(attrs={"class":"form-control"}),
            "yazi" : Textarea(attrs={"class":"form-control"}),
            # "image" : FileInput(attrs={"class":"form-control"}),
            # "image_single" : FileInput(attrs={"class":"form-control"}),
          
        }


