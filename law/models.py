from django.db import models

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
    subject=models.CharField(max_length=250,blank=False,null=False)
    message=models.TextField(blank=False,null=False)
    created_date=models.DateTimeField(auto_now_add=True)
    okundu_mu=models.CharField(max_length=10,choices=STATUS,default="no",verbose_name="Okundu mu?")
       
    class Meta:
        db_table="IletisimModel"
        verbose_name = 'Mesaj'
        verbose_name_plural = 'Gelen Mesajlar'
        
    def __str__(self):  
        return self.isim