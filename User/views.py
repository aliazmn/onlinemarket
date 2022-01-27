from uuid import uuid4

from django.contrib.auth import authenticate, logout as _logout, login as _login,get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.db.models import Q
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.core.cache import cache

from project import settings
from User.forms import ForgetPasswordForm, RegisterForm ,LoginForm
from django.core.cache import caches
from .models import Address, Customer, Profile, UserDevice


User = get_user_model()

@require_http_methods(["GET", "POST"])
def login(request):
    login_form = LoginForm(request.POST or None)
    if request.method == "GET":
        return render(request, 'User/login_page.html', {'login_form': login_form})
    else:
        if login_form.is_valid():
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")
            user = authenticate(request, email=email, password=password)
            if user is not None:  
                _login(request, user)
                next = request.GET.get("next", "")
                user=user
                print(user)
                if request.user_agent.is_mobile:
                    device = "Mobile"
                if request.user_agent.is_tablet:
                    device = "Tablet"
                if request.user_agent.is_pc:
                    device = "PC"
                browser=request.user_agent.browser.family
                os=request.user_agent.os.family
                query=UserDevice.objects.filter(Q(user=user)&Q(device=device))
                if not query:
                    UserDevice.objects.create(user=user,device=device,browser=browser,os=os)
                if not request.session.session_key:
                    request.session.save()
                redis_cache=caches['default']
                cart=redis_cache.client.get_client()
                carts=cart.hgetall(request.session.session_key)
                for elm in carts:
                    cart.hset(request.user.email,elm.decode("utf-8"),carts[elm])
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
    print(register_form)
    if request.method == "GET":
        return render(request, 'User/register_page.html', {'register_form': register_form})
    elif request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user=register_form.save(commit=False)
            user.is_active = False
            user.save()
            cus=Customer.objects.create(profile=user)
            address=Address(add=register_form.cleaned_data.get("address"),postalcode=register_form.cleaned_data.get("postal_code"))
            address.save()
            cus.add.add(address)
            cus.save()     
            uid=str(uuid4())
            link=reverse("user:activate",kwargs={"valid":uid})
            current_site = get_current_site(request)
            mail_subject = 'Activate your account on online market.'
            message = "127.0.0.1:8000"+link
            to_email = register_form.cleaned_data.get('email')
            request.session["email"]=to_email
            request.session["uid"]=uid
            cache.set(to_email,uid,180)
            send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])

            
            return redirect('user:login')
        else:
            return render(request, 'User/register_page.html', {'register_form': register_form})

def activate(request, valid):
    user=Profile.objects.get(email=request.session.get("email"))
    ucode=cache.get(request.session.get("email"))
    if request.session.get("uid")==ucode:
        user.is_active=True
        user.save()
        _login(request,user)
        return redirect("home")
    else:
        return redirect("user:register")


def forget_password(request):
    forget_password_form = ForgetPasswordForm(request.POST or None)
    if request.method == "GET":
        return render(request, 'User/forget_password_form.html', {'forget_password_form': forget_password_form})
    else:     
        if forget_password_form.is_valid():
            miss_email=forget_password_form.cleaned_data.get('email')
            #user = authenticate(request, email=miss_email)
            user = User.objects.get(email=miss_email)
            if user:
                link=reverse("user:forget_pass")
                current_site = get_current_site(request)
                mail_subject = 'click on the link for change password.'
                message = "127.0.0.1:8000"+link
                to_email = forget_password_form.cleaned_data.get('email')
                request.session["email"]=to_email
                cache.set(user,to_email,180)
                send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])
                return redirect('user:login')
            else:
                return redirect('user:forget_password')


def forget_pass():
    pass


def user_session_logedin(request):
     if request.method == "GET":
    #     user=request.user.email
    #     print(user)
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




