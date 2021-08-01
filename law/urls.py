from django.urls.conf import include
from django.urls import path
from .views import (
    index,iletisim,hakkimizda,CalismaAlanlari,SingleHakkimizda
)


urlpatterns = [
    path('', index,name="index"),
    path('iletisim',iletisim,name="iletisim"),
    path('hakkimizda',hakkimizda,name="hakkimizda"),
    path('CalismaAlanlari',CalismaAlanlari,name="CalismaAlanlari"),
    path('hakkimizda_single',SingleHakkimizda,name="SingleHakkimizda"),

]

