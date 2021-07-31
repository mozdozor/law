from django.urls.conf import include
from django.urls import path
from .views import (
    index,iletisim
)


urlpatterns = [
    path('', index,name="index"),
    path('iletisim',iletisim,name="iletisim"),

]

