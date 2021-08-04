
from django.urls import path
from .views import (
     indexAdmin,loginAdmin,logoutAdmin,sliderAdmin,sliderUpdateAdmin,sliderEkleAdmin,deleteSliderAdmin,reviewAdmin,
     deleteReviewAdmin,hakkimizdaUpdateAdmin,hakkimizdaAdmin,hakkimizdaEkleAdmin
)


urlpatterns = [
    path('',loginAdmin,name="loginAdmin"),
    path('',logoutAdmin,name="logoutAdmin"),
    path('indexAdmin',indexAdmin,name="indexAdmin"),
    path('sliderAdmin',sliderAdmin,name="sliderAdmin"),
    path('sliderUpdateAdmin/<int:pk>',sliderUpdateAdmin,name="sliderUpdateAdmin"),
    path('sliderEkleAdmin',sliderEkleAdmin,name="sliderEkleAdmin"),
    path('deleteSliderAdmin/<int:pk>',deleteSliderAdmin,name="deleteSliderAdmin"),
    path('reviewAdmin',reviewAdmin,name="reviewAdmin"),
    path('deleteReviewAdmin/<int:pk>',deleteReviewAdmin,name="deleteReviewAdmin"),
    path('hakkimizdaAdmin',hakkimizdaAdmin,name="hakkimizdaAdmin"),
    path('hakkimizdaEkleAdmin',hakkimizdaEkleAdmin,name="hakkimizdaEkleAdmin"),
    path('hakkimizdaUpdateAdmin/<int:pk>',hakkimizdaUpdateAdmin,name="hakkimizdaUpdateAdmin"),
]