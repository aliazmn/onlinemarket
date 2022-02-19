

from django.contrib.auth import authenticate, logout as _logout, login as _login,get_user_model
from django.core.cache import cache


from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.core.cache import cache
from User.utils import linked_devices
from project import settings
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.core.cache import caches


from User.forms import ForgetPassForm, ForgetPasswordForm, RegisterForm ,LoginForm
from .models import Address, Customer, Profile, UserDevice
from .utils import Send_email,make_session
from .tasks import my_validate


from User.forms import ForgetPassForm, ForgetPasswordForm, RegisterForm ,LoginForm
from .models import Address, Customer, Profile, UserDevice
from .utils import filling_cart



User = get_user_model()

@require_http_methods(["GET", "POST"])
def login(request):
    login_form = LoginForm(request.POST or None)
    if request.method == "GET":
        next = request.GET.get("next", "")
        
        if next:
            return render(request, 'User/login_page.html', {'login_form': login_form,'next':next})
        else:
            return render(request, 'User/login_page.html', {'login_form': login_form,})
            
    else:
        if login_form.is_valid():
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")
            user = authenticate(request, email=email, password=password)
            if user is not None:  
                _login(request, user)
                next = request.GET.get("next", "")
                linked_devices(request,user)
                filling_cart(request)
                if next:
                    return redirect(next)
                return redirect('home')
            else:
                 return render(request, 'User/login_page.html', {'login_form': login_form})
        else:
            return render(request, 'User/login_page.html', {'login_form': login_form})


def logout(request):
    _logout(request)
    return redirect('home')


def register(request):
    register_form = RegisterForm(request.POST or None)
    if request.method == "GET":
        return render(request, 'User/register_page.html', {'register_form': register_form})
    elif request.method == "POST":
        if register_form.is_valid():
            user=register_form.save(commit=False)
            user.is_active = False
            user.save()
            cus=Customer.objects.create(profile=user)
            address=Address(add=register_form.cleaned_data.get("address"),postalcode=register_form.cleaned_data.get("postal_code"))
            address.save()
            cus.add.add(address)
            cus.save() 
            opt="activate"
            to_email = register_form.cleaned_data.get('email')
            my_validate.delay(request,to_email,opt)    
            return redirect('user:login')
        else:
            return render(request, 'User/register_page.html', {'register_form': register_form})


def activate(request, valid, backend='django.contrib.auth.backends.ModelBackend'):
    user=Profile.objects.get(email=request.session.get("email"))
    ucode=cache.get(request.session.get("email"))
    if request.session.get("uid")==ucode:
        user.is_active=True
        user.save()
        _login(request,user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect("home")
    else:
        return redirect("user:register")



def forget_password(request):
    forget_password_form = ForgetPasswordForm(request.POST or None)
    if request.method == "GET":
        return render(request, 'User/forget_password.html', {'forget_password_form': forget_password_form})
    else:     
        if forget_password_form.is_valid():
            miss_email=forget_password_form.cleaned_data.get('email')
            user = User.objects.get(email=miss_email)
            if user:
                opt = "forget-pass"
                to_email = forget_password_form.cleaned_data.get('email')
                uid=make_session(request,to_email)
                my_validate.delay(to_email,uid,opt)
                return render(request,'User/forget_status.html',{'status':"please check your email for continue."})
            else:
                return redirect('user:forget_password')



def set_true(request,auten):
    user=Profile.objects.get(email=request.session.get("email"))
    ucode=cache.get(request.session.get("email"))
    if request.session.get("uid")==ucode:
        cache.set("forget",1,300)
        return redirect('user:forget_pass')
        
    else:
        return render(request,"User/forget_password.html")

        

def forget_pass(request):
    forget_pass_form = ForgetPassForm(request.POST or None)
    if request.method == "GET":
        return render(request, 'User/forget_pass.html', {'forget_pass_form': forget_pass_form})
    else:
        user=Profile.objects.get(email=request.session.get("email"))
        ucode=cache.get(request.session.get("email"))
        if request.session.get("uid")==ucode:
                forg=cache.get("forget")
                if forg:
                    if forget_pass_form.is_valid():
                        password = request.POST.get("password", "")
                        user.set_password(password)
                        user.save()
                        user = authenticate(request, email=request.session.get("email"), password=password)
                        _login(request,user)
                        return redirect("home")
                    else:
                        return render(request,"User/forget_pass.html")
                else:
                    return render(request, "User/forget_pass.html")
        else:
            return render(request,"User/forget_password.html")


# @login_required
class show_profile(DetailView):
    model=Profile
    template_name="User/profile.html"
    context_object_name="profile_item"
    pk_url_kwarg="id"






def user_session_logedin(request):
     if request.method == "GET":
    #     user=request.user.email
    #     if request.user_agent.is_mobile:
    #         device = "Mobile"
    #     if request.user_agent.is_tablet:
    #         device = "Tablet"
    #     if request.user_agent.is_pc:
    #         device = "PC"
    #     browser=request.user_agent.browser.family
    #     os=request.user_agent.os.family
    #     query=UserDevice.objects.filter(Q(user=user)&Q(device=device))
    #     if not query:
    #         UserDevice.objects.create(user=user,device=device,browser=browser,os=os)
        linked_devices=UserDevice.objects.all()
        ctx={
            'linked_devices':linked_devices
        }
        return render(request,'session.html',ctx)

def delet_session(request):
    pass


