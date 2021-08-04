
from law.forms import HakkimizdaModelForm, SliderModelForm
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,update_session_auth_hash
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import logout
from law.models import HakkimizdaModel, ReviewModel, SliderModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm





@permission_required('is_staff',login_url="loginAdmin")
def indexAdmin(request):
    return render(request,"indexAdmin.html",{})




def loginAdmin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)		
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect("indexAdmin")
            else:
                messages.error(request,"Kullanıcı adı ya da parolanız hatalıdır.")
        else:
            messages.error(request,"Kullanıcı adı ya da parolanız hatalıdır.")
    form = AuthenticationForm()
    return render(request=request, template_name="loginAdmin.html", context={"form":form})




def logoutAdmin(request):
    logout(request)
    return redirect("loginAdmin")





@permission_required('is_staff',login_url="loginAdmin")
def sliderAdmin(request):
    sliders=SliderModel.objects.all()
    context={
        "sliders":sliders,
    }
    return render(request,"sliderAdmin.html",context)



@permission_required('is_staff',login_url="loginAdmin")
def sliderUpdateAdmin(request,pk):
    slider=get_object_or_404(SliderModel,pk=pk)
    form=SliderModelForm(instance=slider)    
    if request.method == "POST":
        form = SliderModelForm(request.POST,request.FILES,instance=slider)
        if form.is_valid():
            form.save()
            messages.success(request,'Güncelleme başarıyla tamamlanmıştır')
            return redirect("sliderUpdateAdmin",pk=slider.pk)
        else:
            messages.error(request,"Lütfen gereken alanları eksiksiz bir şekilde doldurunuz")
            return redirect("sliderUpdateAdmin" ,pk=slider.pk)   
    context={
        "form":form,
        "slider":slider,
    }
    return render(request,"sliderUpdateAdmin.html",context)




@permission_required('is_staff',login_url="loginAdmin")
def sliderEkleAdmin(request):
    if request.method == "POST":
        form = SliderModelForm(request.POST or None, files=request.FILES or None)		
        if form.is_valid():
            form.save()    
            messages.success(request,"Slider başarıyla eklenmiştir")
        else:
            messages.error(request,"Slider eklerken hata oluştu.Lütfen alanları gerektiği gibi doldurunuz")
    form = SliderModelForm()
    return render(request=request, template_name="sliderEkleAdmin.html", context={"form":form})





@permission_required('is_staff',login_url="loginAdmin")
def deleteSliderAdmin(request,pk):
    slider=get_object_or_404(SliderModel,pk=pk)
    slider.delete()
    return redirect(request.META['HTTP_REFERER']) 







@permission_required('is_staff',login_url="loginAdmin")
def reviewAdmin(request):
    reviews=ReviewModel.objects.all()
    context={
        "reviews":reviews,
    }
    return render(request,"reviewAdmin.html",context)



@permission_required('is_staff',login_url="loginAdmin")
def deleteReviewAdmin(request,pk):
    review=get_object_or_404(ReviewModel,pk=pk)
    review.delete()
    return redirect(request.META['HTTP_REFERER']) 




@permission_required('is_staff',login_url="loginAdmin")
def hakkimizdaAdmin(request):
    hakkimizda=HakkimizdaModel.objects.all()
    context={
        "hakkimizda":hakkimizda,
    }
    return render(request,"hakkimizdaAdmin.html",context)



@permission_required('is_staff',login_url="loginAdmin")
def hakkimizdaUpdateAdmin(request,pk):
    hakkimizda=get_object_or_404(HakkimizdaModel,pk=pk)
    form=HakkimizdaModelForm(instance=hakkimizda)    
    if request.method == "POST":
        form = HakkimizdaModelForm(request.POST,request.FILES,instance=hakkimizda)
        if form.is_valid():
            form.save()
            messages.success(request,'Güncelleme başarıyla tamamlanmıştır')
            return redirect("hakkimizdaUpdateAdmin",pk=hakkimizda.pk)
        else:
            messages.error(request,"Lütfen gereken alanları eksiksiz bir şekilde doldurunuz")
            return redirect("hakkimizdaUpdateAdmin" ,pk=hakkimizda.pk)   
    context={
        "form":form,
        "hakkimizda":hakkimizda,
    }
    return render(request,"hakkimizdaUpdateAdmin.html",context)





@permission_required('is_staff',login_url="loginAdmin")
def hakkimizdaEkleAdmin(request):
    if request.method == "POST":
        form = HakkimizdaModelForm(request.POST or None, files=request.FILES or None)		
        if form.is_valid():
            HakkimizdaModel.objects.all().delete()
            form.save()    
            messages.success(request,"Hakkımızda modeli başarıyla eklenmiştir")
        else:
            messages.error(request,"Hakkımızda modeli eklenirken hata oluştu.Lütfen alanları gerektiği gibi doldurunuz")
    form = HakkimizdaModelForm()
    return render(request=request, template_name="hakkimizdaEkleAdmin.html", context={"form":form})
