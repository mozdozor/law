from ckeditor import fields
from ckeditor.fields import RichTextField, RichTextFormField
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.db.models.query_utils import FilteredRelation
from django.forms.fields import EmailField
from django.forms.widgets import EmailInput, FileInput, HiddenInput, NumberInput, Select, TextInput ,Textarea
from .models import AlanModel, AvukatModel, HakkimizdaModel, IletisimBilgilerModel, IletisimModel, NedenBizImageModel, NedenBizModeli, ReviewModel,SliderModel, TimelineModel
from django.contrib.auth.forms import UserCreationForm





class UserForm(forms.ModelForm):
    password=None
    class Meta:
        model = User
        fields=("username","first_name","last_name","email",)
        widgets = {
            "username" : TextInput(attrs={"style":"text-transform: none;","class":"form-control"}),
            "first_name" : TextInput(attrs={"style":"text-transform: none;","class":"form-control"}),
            "last_name" : TextInput(attrs={"style":"text-transform: none;","class":"form-control"}),
            "email" : EmailInput(attrs={"style":"text-transform: none;","type":"email","class":"form-control"}),
          
        }



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




class TimelineModelForm(forms.ModelForm):
    class Meta:
        model = TimelineModel
        exclude = ('created_date','updated_date')
        widgets = {
            "title" : TextInput(attrs={"class":"form-control"}),
            "yazi" : Textarea(attrs={"class":"form-control"}),
            "tarih" : NumberInput(attrs={"class":"form-control"}),                  
        }



class AvukatModelForm(forms.ModelForm):
    class Meta:
        model = AvukatModel
        exclude = ('created_date','updated_date')
        widgets = {
            "name" : TextInput(attrs={"class":"form-control"}),
            "alan" : TextInput(attrs={"class":"form-control"}),
          #  "image" : NumberInput(attrs={"class":"form-control"}),   
            "twitter" : TextInput(attrs={"class":"form-control"}),
            "facebook" : TextInput(attrs={"class":"form-control"}),
            "instagram" : TextInput(attrs={"class":"form-control"}),
            "linkedin" : TextInput(attrs={"class":"form-control"}),               
        }



class AlanModelForm(forms.ModelForm):
    class Meta:
        model = AlanModel
        exclude = ('created_date','updated_date')
        widgets = {
            "name" : TextInput(attrs={"class":"form-control"}),
            "content" : Textarea(attrs={"class":"form-control"}),
            "icon" : TextInput(attrs={"class":"form-control"}),                  
        }





class NedenBizModelForm(forms.ModelForm):
    class Meta:
        model = NedenBizModeli
        exclude = ('created_date','updated_date')
        widgets = {
            "title" : TextInput(attrs={"class":"form-control"}),
            "content" : Textarea(attrs={"class":"form-control"}),
            "icon" : TextInput(attrs={"class":"form-control"}),                  
        }



class NedenBizImageModelForm(forms.ModelForm):
    class Meta:
        model = NedenBizImageModel
        fields = ('image',)
        # widgets = {
        #     "title" : TextInput(attrs={"class":"form-control"}),
        #     "content" : Textarea(attrs={"class":"form-control"}),
        #     "icon" : TextInput(attrs={"class":"form-control"}),                  
        # }





class IletisimBilgilerModelForm(forms.ModelForm):
    class Meta:
        model = IletisimBilgilerModel
        fields = ('__all__')
        widgets = {
            "konum" : Textarea(attrs={"class":"form-control"}),
            "telefon" : TextInput(attrs={"class":"form-control"}),
            "email" : EmailInput(attrs={"class":"form-control"}),   
            "twitter" : TextInput(attrs={"class":"form-control"}),
            "facebook" : TextInput(attrs={"class":"form-control"}),
            "instagram" : TextInput(attrs={"class":"form-control"}),
            "linkedin" : TextInput(attrs={"class":"form-control"}),               
        }





class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        exclude = ('created_date','updated_date')
        widgets = {
            "name" : TextInput(attrs={"class":"form-control"}),
            "dava" : TextInput(attrs={"class":"form-control"}),
            "review" : Textarea(attrs={"class":"form-control"})       
        }


