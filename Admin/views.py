
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,update_session_auth_hash
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import logout

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


