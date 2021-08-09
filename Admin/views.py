
from law.forms import AlanModelForm, AvukatModelForm, HakkimizdaModelForm, IletisimBilgilerModelForm, NedenBizImageModelForm, NedenBizModelForm, SliderModelForm, TimelineModelForm, UserForm
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,update_session_auth_hash
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import logout
from law.models import AlanModel, AvukatModel, HakkimizdaModel, IletisimBilgilerModel, IletisimModel, NedenBizImageModel, NedenBizModeli, ReviewModel, SliderModel, TimelineModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm,UserChangeForm





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
    paginator = Paginator(sliders, 10)  # 6 posts in each page
    page = request.GET.get('page')
    try:
        sliders = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        sliders = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        sliders = paginator.page(paginator.num_pages)
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
    paginator = Paginator(reviews, 10)  # 6 posts in each page
    page = request.GET.get('page')
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        reviews = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        reviews = paginator.page(paginator.num_pages)
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





@permission_required('is_staff',login_url="loginAdmin")
def deleteHakkimizdaAdmin(request,pk):
    hakkimizda=get_object_or_404(HakkimizdaModel,pk=pk)
    hakkimizda.delete()
    return redirect(request.META['HTTP_REFERER']) 




@permission_required('is_staff',login_url="loginAdmin")
def TimelineAdmin(request):
    timelines=TimelineModel.objects.all().order_by("-tarih")
    paginator = Paginator(timelines, 10)  # 6 posts in each page
    page = request.GET.get('page')
    try:
        timelines = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        timelines = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        timelines = paginator.page(paginator.num_pages)
    context={
        "timelines":timelines,
    }
    return render(request,"timelineAdmin.html",context)




@permission_required('is_staff',login_url="loginAdmin")
def deleteTimelineAdmin(request,pk):
    timeline=get_object_or_404(TimelineModel,pk=pk)
    timeline.delete()
    return redirect(request.META['HTTP_REFERER']) 




@permission_required('is_staff',login_url="loginAdmin")
def TimelineUpdateAdmin(request,pk):
    item=get_object_or_404(TimelineModel,pk=pk)
    form=TimelineModelForm(instance=item)    
    if request.method == "POST":
        form = TimelineModelForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,'Güncelleme başarıyla tamamlanmıştır')
            return redirect("TimelineUpdateAdmin",pk=item.pk)
        else:
            messages.error(request,"Lütfen gereken alanları eksiksiz bir şekilde doldurunuz")
            return redirect("TimelineUpdateAdmin" ,pk=item.pk)   
    context={
        "form":form,
        "item":item,
        "update":"update",
    }
    return render(request,"timelineUpdateAdmin.html",context)




@permission_required('is_staff',login_url="loginAdmin")
def TimelineEkleAdmin(request):
    if request.method == "POST":
        form = TimelineModelForm(request.POST or None, files=request.FILES or None)		
        if form.is_valid():
            form.save()    
            messages.success(request,"Zaman çizelgesi başarıyla eklenmiştir")
        else:
            messages.error(request,"Zaman çizelgesi eklenirken hata oluştu.Lütfen alanları gerektiği gibi doldurunuz")
    form = TimelineModelForm()
    context={
        "form":form,
        "create":"create",
    }
    return render(request=request, template_name="timelineUpdateAdmin.html",context=context)





@permission_required('is_staff',login_url="loginAdmin")
def AvukatlarAdmin(request):
    avukatlar=AvukatModel.objects.all()
    paginator = Paginator(avukatlar, 10)  # 6 posts in each page
    page = request.GET.get('page')
    try:
        avukatlar = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        avukatlar = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        avukatlar = paginator.page(paginator.num_pages)
    context={
        "avukatlar":avukatlar,
    }
    return render(request,"avukatlar.html",context)




@permission_required('is_staff',login_url="loginAdmin")
def AvukatUpdateAdmin(request,pk):
    item=get_object_or_404(AvukatModel,pk=pk)
    form=AvukatModelForm(instance=item)    
    if request.method == "POST":
        form = AvukatModelForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,'Güncelleme başarıyla tamamlanmıştır')
            return redirect("AvukatUpdateAdmin",pk=item.pk)
        else:
            messages.error(request,"Lütfen gereken alanları eksiksiz bir şekilde doldurunuz")
            return redirect("AvukatUpdateAdmin" ,pk=item.pk)   
    context={
        "form":form,
        "item":item,
        "update":"update",
    }
    return render(request,"avukatUpdateAdmin.html",context)






@permission_required('is_staff',login_url="loginAdmin")
def AvukatEkleAdmin(request):
    if request.method == "POST":
        form = AvukatModelForm(request.POST or None, files=request.FILES or None)		
        if form.is_valid():
            form.save()    
            messages.success(request,"Avukat başarıyla eklenmiştir")
        else:
            messages.error(request,"Avukat eklenirken hata oluştu.Lütfen alanları gerektiği gibi doldurunuz")
    form = AvukatModelForm()
    context={
        "form":form,
        "create":"create",
    }
    return render(request=request, template_name="avukatUpdateAdmin.html",context=context)




@permission_required('is_staff',login_url="loginAdmin")
def deleteAvukatAdmin(request,pk):
    avukat=get_object_or_404(AvukatModel,pk=pk)
    avukat.delete()
    return redirect(request.META['HTTP_REFERER']) 





@permission_required('is_staff',login_url="loginAdmin")
def CalismaAlanlariAdmin(request):
    alanlar=AlanModel.objects.all()
    paginator = Paginator(alanlar, 10)  # 6 posts in each page
    page = request.GET.get('page')
    try:
        alanlar = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        alanlar = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        alanlar = paginator.page(paginator.num_pages)
    context={
        "alanlar":alanlar,
    }
    return render(request,"calismaAlanlariAdmin.html",context)



@permission_required('is_staff',login_url="loginAdmin")
def AlanUpdateAdmin(request,pk):
    item=get_object_or_404(AlanModel,pk=pk)
    form=AlanModelForm(instance=item)    
    if request.method == "POST":
        form = AlanModelForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,'Güncelleme başarıyla tamamlanmıştır')
            return redirect("AlanUpdateAdmin",pk=item.pk)
        else:
            messages.error(request,"Lütfen gereken alanları eksiksiz bir şekilde doldurunuz")
            return redirect("AlanUpdateAdmin" ,pk=item.pk)   
    context={
        "form":form,
        "item":item,
        "update":"update",
    }
    return render(request,"alanUpdateAdmin.html",context)





@permission_required('is_staff',login_url="loginAdmin")
def AlanEkleAdmin(request):
    if request.method == "POST":
        form = AlanModelForm(request.POST or None, files=request.FILES or None)		
        if form.is_valid():
            form.save()    
            messages.success(request,"Çalışma alanı başarıyla eklenmiştir")
        else:
            messages.error(request,"Çalışma alanı eklenirken hata oluştu.Lütfen alanları gerektiği gibi doldurunuz")
    form = AlanModelForm()
    context={
        "form":form,
        "create":"create",
    }
    return render(request=request, template_name="alanUpdateAdmin.html",context=context)




@permission_required('is_staff',login_url="loginAdmin")
def deleteAlanAdmin(request,pk):
    alan=get_object_or_404(AlanModel,pk=pk)
    alan.delete()
    return redirect(request.META['HTTP_REFERER']) 






@permission_required('is_staff',login_url="loginAdmin")
def NedenBizAdmin(request):
    nedenbizler=NedenBizModeli.objects.all()
    image=NedenBizImageModel.objects.all().first()
    context={
        "nedenbizler":nedenbizler,
        "image":image,
    }
    return render(request,"nedenBizAdmin.html",context)



@permission_required('is_staff',login_url="loginAdmin")
def NedenBizUpdateAdmin(request,pk):
    item=get_object_or_404(NedenBizModeli,pk=pk)
    form=NedenBizModelForm(instance=item)    
    if request.method == "POST":
        form = NedenBizModelForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,'Güncelleme başarıyla tamamlanmıştır')
            return redirect("NedenBizUpdateAdmin",pk=item.pk)
        else:
            messages.error(request,"Lütfen gereken alanları eksiksiz bir şekilde doldurunuz")
            return redirect("NedenBizUpdateAdmin" ,pk=item.pk)   
    context={
        "form":form,
        "item":item,
        "update":"update",
    }
    return render(request,"NedenBizUpdateAdmin.html",context)




@permission_required('is_staff',login_url="loginAdmin")
def NedenBizEkleAdmin(request):
    if request.method == "POST":
        form = NedenBizModelForm(request.POST or None, files=request.FILES or None)		
        if form.is_valid():
            form.save()    
            messages.success(request,"Alan başarıyla eklenmiştir")
        else:
            messages.error(request,"Alan eklenirken hata oluştu.Lütfen alanları gerektiği gibi doldurunuz")
    form = NedenBizModelForm()
    context={
        "form":form,
        "create":"create",
    }
    return render(request=request, template_name="NedenBizUpdateAdmin.html",context=context)





@permission_required('is_staff',login_url="loginAdmin")
def deleteNedenBizAdmin(request,pk):
    alan=get_object_or_404(NedenBizModeli,pk=pk)
    alan.delete()
    return redirect(request.META['HTTP_REFERER']) 







@permission_required('is_staff',login_url="loginAdmin")
def NedenBizImageUpdateAdmin(request,pk):
    item=get_object_or_404(NedenBizImageModel,pk=pk)
    form=NedenBizImageModelForm(instance=item)    
    if request.method == "POST":
        form = NedenBizImageModelForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,'Güncelleme başarıyla tamamlanmıştır')
            return redirect("NedenBizImageUpdateAdmin",pk=item.pk)
        else:
            messages.error(request,"Lütfen gereken alanları eksiksiz bir şekilde doldurunuz")
            return redirect("NedenBizImageUpdateAdmin" ,pk=item.pk)   
    context={
        "form":form,
        "item":item,
        "updateimage":"updateimage",
    }
    return render(request,"NedenBizUpdateAdmin.html",context)





@permission_required('is_staff',login_url="loginAdmin")
def NedenBizImageEkleAdmin(request):
    if request.method == "POST":
        form = NedenBizImageModelForm(request.POST or None, files=request.FILES or None)		
        if form.is_valid():
            NedenBizImageModel.objects.all().delete()
            form.save()    
            messages.success(request,"Fotoğraf başarıyla eklenmiştir")
        else:
            messages.error(request,"Fotoğraf eklenirken hata oluştu.Lütfen alanları gerektiği gibi doldurunuz")
    form = NedenBizImageModelForm()
    context={
        "form":form,
        "createimage":"createimage",
    }
    return render(request=request, template_name="NedenBizUpdateAdmin.html",context=context)




@permission_required('is_staff',login_url="loginAdmin")
def showProfileAdmin(request):
    form=UserForm(instance=request.user)
    context={
        "form":form,
    }
    return render(request,"profileAdmin.html",context)



@permission_required('is_staff',login_url="loginAdmin")
def updateProfileAdmin(request):
    if request.method == "POST":
        form = UserForm(request.POST or None,request.FILES or None,instance=request.user)   
        if form.is_valid():
            form.save()             
            messages.success(request,'Profiliniz başarıyla güncellendi!')
            return redirect("updateProfileAdmin")
        else:
            messages.error(request,form.errors)
            return redirect("updateProfileAdmin")

    form=UserForm(instance=request.user)
    context={
        "form":form,
        
    }
    return render(request,"profileUpdateAdmin.html",context)




@permission_required('is_staff',login_url="loginAdmin")
def changePasswordAdmin(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()           
            update_session_auth_hash(request, user)  # Important!
            messages.success(request,'Şifreniz başarıyla güncellendi!')
            return redirect("changePasswordAdmin")
        else:
            messages.error(request,"Hata! Lütfen gereken yerleri aşağıda yazıldığı gibi doldurunuz")
            return redirect("changePasswordAdmin")

    form=PasswordChangeForm(request.user)
    context={
        "form":form,
    }
    return render(request,"passwordChangeAdmin.html",context)




@permission_required('is_staff',login_url="loginAdmin")
def mailListAdmin(request):
    mails=IletisimModel.objects.all().order_by('pk')
    context={
        "mails":mails,
    }
    return render(request,"mailListAdmin.html",context)


@permission_required('is_staff',login_url="loginAdmin")
def showMessage(request,pk):
    email=get_object_or_404(IletisimModel,pk=pk)
    email.okundu_mu = "yes"
    email.save()
    context={
        "email":email,
    }
    return render(request,"showMessage.html",context)




@permission_required('is_staff',login_url="loginAdmin")
def deleteEmailAdmin(request,pk):
    email=get_object_or_404(IletisimModel,pk=pk)
    email.delete()
    return redirect("mailListAdmin") 




@permission_required('is_staff',login_url="loginAdmin")
def IletisimBilgilerAdmin(request):
    iletisim=IletisimBilgilerModel.objects.all().first()
    context={
        "iletisim":iletisim,
      
    }
    return render(request,"IletisimBilgilerAdmin.html",context)



@permission_required('is_staff',login_url="loginAdmin")
def IletisimBilgilerUpdateAdmin(request,pk):
    item=get_object_or_404(IletisimBilgilerModel,pk=pk)
    form=IletisimBilgilerModelForm(instance=item)    
    if request.method == "POST":
        form = IletisimBilgilerModelForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,'Güncelleme başarıyla tamamlanmıştır')
            return redirect("IletisimBilgilerUpdateAdmin",pk=item.pk)
        else:
            messages.error(request,"Lütfen gereken alanları eksiksiz bir şekilde doldurunuz")
            return redirect("IletisimBilgilerUpdateAdmin" ,pk=item.pk)   
    context={
        "form":form,
        "item":item,
        "update":"update",
    }
    return render(request,"IletisimBilgilerUpdateAdmin.html",context)





@permission_required('is_staff',login_url="loginAdmin")
def IletisimBilgilerEkleAdmin(request):
    if request.method == "POST":
        form = IletisimBilgilerModelForm(request.POST or None, files=request.FILES or None)		
        if form.is_valid():
            IletisimBilgilerModel.objects.all().delete()
            form.save()    
            messages.success(request,"İletişim bilgileriniz başarıyla eklenmiştir")
        else:
            messages.error(request,"İletişim bilgileriniz eklenirken hata oluştu.Lütfen alanları gerektiği gibi doldurunuz")
    form = IletisimBilgilerModelForm()
    context={
        "form":form,
        "create":"create",
    }
    return render(request=request, template_name="IletisimBilgilerUpdateAdmin.html",context=context)




@permission_required('is_staff',login_url="loginAdmin")
def showUsersAdmin(request):
    users=User.objects.all()
    context={
        "users":users,
    }
    return render(request,"usersAdmin.html",context)

