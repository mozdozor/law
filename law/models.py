from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser, User

# Create your models here.





class SliderModel(models.Model):
    
    STATUS = (
        ("yes" , "YES"),
        ("no" , "NO")
    )
    image=models.ImageField(
        upload_to="slider_images",
    )
    main_title=models.CharField(
        max_length=250,
        blank=False,
        null=False
    )
    top_title=models.CharField(
        max_length=250,
        blank=False,
        null=False
    )
    bottom_title=models.CharField(
        max_length=250,
        blank=False,
        null=False
    )
    is_slider=models.CharField(max_length=10,choices=STATUS,default="no",verbose_name="Slider olsun mu?")
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
   

    class Meta:
        db_table="slider"
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliderlar'

    def __str__(self):
        return self.main_title


class IletisimBilgilerModel(models.Model):
    konum=models.CharField(max_length=250,blank=False,null=False)
    telefon=models.CharField(max_length=250,blank=False,null=False)
    email=models.CharField(max_length=250,blank=False,null=False)
    twitter=models.CharField(max_length=100,blank=False,null=False)
    facebook=models.CharField(max_length=100,blank=True,null=True)
    linkedin=models.CharField(max_length=100,blank=True,null=True)
    instagram=models.CharField(max_length=100,blank=True,null=True)
       
    class Meta:
        db_table="IletisimBilgiler"
        verbose_name = 'İletişim Bilgileri'
        verbose_name_plural = 'İletişim Bilgilerimiz'
        
    def __str__(self):
        return self.email


class IletisimModel(models.Model):
    STATUS = (
        ("yes" , "YES"),
        ("no" , "NO")
    )
    isim=models.CharField(max_length=250,blank=False,null=False)
    email=models.CharField(max_length=250,blank=False,null=False)
    subject=models.CharField(max_length=250,blank=False,null=False,verbose_name="Konu")
    phone=models.CharField(max_length=11,blank=False,null=False,verbose_name="Telefon")
    message=models.TextField(blank=False,null=False,verbose_name="Mesaj")
    created_date=models.DateTimeField(auto_now_add=True)
    okundu_mu=models.CharField(max_length=10,choices=STATUS,default="no",verbose_name="Okundu mu?")
       
    class Meta:
        db_table="IletisimModel"
        verbose_name = 'Mesaj'
        verbose_name_plural = 'Gelen Mesajlar'
        
    def __str__(self):  
        return self.isim




class HakkimizdaModel(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False)
    yazi=RichTextUploadingField(blank=False,null=False)
    image=models.ImageField(
        upload_to="hakkimizda_images",verbose_name="Anasayfa Fotoğrafı"
    )
    image_single=models.ImageField(
        upload_to="hakkimizda_images",default="",verbose_name="Tek Sayfa Hakkımızda Fotoğrafı"
    )
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
       
    class Meta:
        db_table="HakkimizdaModel"
        verbose_name = 'Hakkımızda'
        verbose_name_plural = 'Hakkımızda'
        
    def __str__(self):  
        return self.title




class TimelineModel(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False)
    yazi=models.TextField(max_length=300,blank=False,null=False)
    tarih=models.SmallIntegerField(blank=False,null=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
       
    class Meta:
        db_table="TimelineModel"
        verbose_name = 'Zaman Çizelgesi'
        verbose_name_plural = 'Zaman Çizelgeleri'
        
    def __str__(self):  
        return self.tarih





class AvukatModel(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    alan=models.CharField(max_length=200,blank=False,null=False)
    image=models.ImageField(
        upload_to="avukat_images",
    )
    twitter=models.CharField(max_length=100,blank=True,null=True)
    facebook=models.CharField(max_length=100,blank=True,null=True)
    linkedin=models.CharField(max_length=100,blank=True,null=True)
    instagram=models.CharField(max_length=100,blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
       
    class Meta:
        db_table="AvukatModel"
        verbose_name = 'Avukat'
        verbose_name_plural = 'Avukatlar'
        
    def __str__(self):  
        return self.name




class AlanModel(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    content=models.CharField(max_length=200,blank=False,null=False)
    icon=models.CharField(max_length=100,blank=False,null=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
       
    class Meta:
        db_table="AlanModel"
        verbose_name = 'Çalışma Alanı'
        verbose_name_plural = 'Çalışma Alanları'
        
    def __str__(self):  
        return self.name




class NedenBizModeli(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False)
    content=models.CharField(max_length=200,blank=False,null=False)
    icon=models.CharField(max_length=100,blank=False,null=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
       
    class Meta:
        db_table="NedenBizModeli"
        verbose_name = 'Neden Bizi Seçmelisiniz?'
        verbose_name_plural = 'Neden Biz'
        
    def __str__(self):  
        return self.title


class NedenBizImageModel(models.Model):
    image=models.ImageField(
        upload_to="nedenbiz_image",
    )
    class Meta:
        db_table="NedenBizImageModel"
        verbose_name = 'Neden Biz Fotoğraf'
        verbose_name_plural = 'Neden Biz Fotosu'
        
    def __str__(self):  
        return self.image.url





class SoruModel(models.Model):
    question=models.CharField(max_length=250,blank=False,null=False)
    answer=RichTextField(blank=False,null=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
       
    class Meta:
        db_table="SoruModel"
        verbose_name = 'Soru'
        verbose_name_plural = 'Sorular'
        
    def __str__(self):  
        return self.question



class ReviewModel(models.Model):
    name=models.CharField(max_length=250,blank=False,null=False)
    dava=models.CharField(max_length=250,blank=False,null=False)
    review=RichTextField(max_length=200,blank=False,null=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
       
    class Meta:
        db_table="ReviewModel"
        verbose_name = 'Müşteri Değerlendirmesi'
        verbose_name_plural = 'Müşteri Değerlendirmeleri'
        
    def __str__(self):  
        return self.dava


