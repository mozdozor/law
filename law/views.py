from django.http import request
from django.shortcuts import render
from .models import AlanModel, AvukatModel, HakkimizdaModel, NedenBizImageModel, NedenBizModeli, SliderModel,IletisimBilgilerModel, TimelineModel
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



def hakkimizda(request): 
    hakkimizda=HakkimizdaModel.objects.first()
    timelines=TimelineModel.objects.all()
    avukatlar=AvukatModel.objects.all()
    context = {
        "hakkimizda":hakkimizda,
        "timelines":timelines,
        "avukatlar":avukatlar,
    }
    return render(request,"hakkimizda.html",context)



def CalismaAlanlari(request): 
    alanlar=AlanModel.objects.all()
    nedenbizler=NedenBizModeli.objects.all()
    image=NedenBizImageModel.objects.first()
    context = {
        "alanlar":alanlar,
        "nedenbizler":nedenbizler,
        "image":image,
    }
    return render(request,"alanlarımız.html",context)




def SingleHakkimizda(request): 
    hakkimizda=HakkimizdaModel.objects.first()
    context = {
       "hakkimizda":hakkimizda,
    }
    return render(request,"single_hakkimizda.html",context)

