from urllib import request
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirectBase, HttpResponseServerError
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from uuid import uuid4
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, logout as _logout, login as _login
from django.core.cache import cache
from project import settings

from User.forms import ForgetPassForm, ForgetPasswordForm, RegisterForm ,LoginForm


from .models import Address, Customer, Profile


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
                if next:
                    return redirect(next)
                return redirect('home')

            else:
                 return render(request, 'User/login_page.html', {'login_form': login_form})


        else:
            return render(request, 'User/login_page.html', {'login_form': login_form})

                





# @require_http_methods(["GET", "POST"])
# def login(request):
#     if request.method == "GET":
#         ctx = {}
#         next = request.GET.get("next", "")
#         if next:
#             ctx["next"] = next
#         return render(request, "User/login.html", ctx)
#     else:
#         email = request.POST.get("email", "")
#         password = request.POST.get("password", "")
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             _login(request, user)
#             next = request.GET.get("next", "")
#             if next:
#                 return redirect(next)
#             return redirect('home')
#         else:
#             return redirect('users:login')


def logout(request):
    _logout(request)
    return redirect('home')

def register(request):
    register_form = RegisterForm(request.POST or None)
    print(register_form)

    if request.method == "GET":
        return render(request, 'User/register_page.html', {'register_form': register_form})
    elif request.method == "POST":
        # register_form = RegisterForm(request.POST)
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




            

# def profile_user(request):
#     courect_user=request.id()
#     qs=Profile.objects.values(courect_user=id)

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
                uid=str(uuid4())
                link=reverse("user:set_True",kwargs={"auten":uid})
                current_site = get_current_site(request)
                mail_subject = 'click on the link for change password.'
                message = "127.0.0.1:8000"+link
                to_email = forget_password_form.cleaned_data.get('email')
                # forget= f'{to_email}+flag'
                # request.session["forget"]=forget
                request.session["email"]=to_email
                request.session["uid"]=uid
                cache.set(to_email,uid,300)
                cache.set("forget",False,300)

                send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])

                return redirect('user:forget_pass')

            else:
                return redirect('user:forget_password')


def set_true():
    user=Profile.objects.get(email=request.session.get("email"))
    ucode=cache.get(request.session.get("email"))
    if request.session.get("uid")==ucode:
        cache.set("forget",True,300)
        return # now you can set new password
        
    else:
        return #link motabar nist
        


def forget_pass(request,auten):
    forget_pass_form = ForgetPassForm(request.POST or None)
    if request.method == "GET":
        return render(request, 'User/forget_pass_form.html', {'forget_pass_form': forget_pass_form})
    
    else:
        user=Profile.objects.get(email=request.session.get("email"))
        ucode=cache.get(request.session.get("email"))
        if request.session.get("uid")==ucode:
                forg=cache.get("forget")
                if forg:
                    if ForgetPassForm.is_valid():
                        password = request.POST.get("password", "")
                        user.set_password(password)
                        user.save()

                        _login(request,user)
                        return redirect("home")
                    else:
                        return redirect("user:forget_password")
                else:
                    return #bayad montazer taiid email bashid
        else:
            return #link taiid eshtebah ast





