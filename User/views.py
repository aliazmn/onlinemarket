from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, logout as _logout, login as _login

from User.forms import RegisterForm ,LoginForm


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
                return render(request, 'User/register_page.html', {'register_form': login_form})

        else:
            return render(request, 'User/register_page.html', {'register_form': login_form})
                





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


    if request.method == "GET":
        return render(request, 'User/register_page.html', {'register_form': register_form})
    elif request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user=register_form.save()
            cus=Customer.objects.create(profile=user)
            address=Address(add=register_form.cleaned_data.get("address"),postalcode=register_form.cleaned_data.get("postal_code"))
            address.save()
            cus.add.add(address)
            cus.save()
            
            
            return redirect('/')
        else:
            return render(request, 'User/register_page.html', {'register_form': register_form})



#============save ro super kon add kon address ro bad bd save she

# def save(self, commit=True):
#     Profile = super(Profile,self).save(commit=False)
#     Profile= self.
    
#     Profile.save()
#     return Profile
            

def profile_user(request):
    courect_user=request.id()
    qs=Profile.objects.values(courect_user=id)


