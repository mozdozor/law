
from django.urls import path
from .views import (
     indexAdmin,loginAdmin,logoutAdmin,
)


urlpatterns = [
    path('',loginAdmin,name="loginAdmin"),
    path('',logoutAdmin,name="logoutAdmin"),
    path('indexAdmin',indexAdmin,name="indexAdmin"),
    
]