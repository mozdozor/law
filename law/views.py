from django.http import request
from django.shortcuts import render
from .models import SliderModel,IletisimBilgilerModel
from .forms import IletisimModelForm
from django.core.mail import send_mail
# Create your views here.


def index(request):
    sliders=SliderModel.objects.filter(is_slider="yes")
    context = {
        "sliders":sliders,
    }
    return render(request,"index.html",context)





def iletisim(request):
    if request.method == "POST":
        form = IletisimModelForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                form.cleaned_data["subject"]+" ( "+form.cleaned_data["isim"]+" )",
                form.cleaned_data["message"]+"\n\n\n ( "+form.cleaned_data["email"]+" )",
                form.cleaned_data["email"],
                [IletisimBilgilerModel.objects.first().email,],
            )
    form = IletisimModelForm()
    bilgiler=IletisimBilgilerModel.objects.first()
    context={
        "form":form,
        "bilgiler":bilgiler,
    }
    return render(request,"iletişim.html",context)
