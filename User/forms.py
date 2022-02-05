from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model,password_validation

from django.forms import ModelForm, ValidationError, widgets, TextInput, EmailInput, PasswordInput

from django.forms.fields import CharField, EmailField
from django.utils.translation import gettext_lazy as _
from User.models import Customer,Profile
from django.core.validators import EmailValidator



User = get_user_model()



class RegisterForm(forms.ModelForm):
    re_password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را تکرار نمایید', 'type':'password', 'required':'', 'class':'e-field-inner'}),label='تکرار رمزعبور')
    
    class Meta:
        model = Profile

        
        fields = ['first_name',"last_name",'email','password',"re_password","address","postal_code"]

        widgets = {
            'first_name': TextInput(attrs={"background-color":"red",'placeholder': 'لطفا نام  خود را وارد نمایید', 'type':'text', 'required':'', 'class':'e-field-inner'}),
            'last_name': TextInput(attrs={'placeholder': 'لطفا نام خانوادگی خود را وارد نمایید', 'type':'text', 'required':'', 'class':'e-field-inner'}),
            'email': EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید', 'type':'email', 'required':'', 'class':'e-field-inner'}),
            'password': PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'type':'password', 'required':'', 'class':'e-field-inner', "id":"password"}),
            'address': TextInput(attrs={'placeholder': 'لطفا ادرس خود را وارد نمایید', 'type':'text', 'required':'', 'class':'e-field-inner'}),
            'postal_code':TextInput(attrs={'placeholder': 'لطفا کدپستی خود را وارد نمایید', 'type':'text', 'required':'', 'class':'e-field-inner'}),
        }

        labels = {
            'first_name' : _('نام'),
            'last_name' : _('نام خانوادگی'),
            'email' : _('ایمیل'),
            'password' : _('رمزعبور'),
            're_password' :'تکرار رمزعبور',
            'address' : _('ادرس'),
            'postal_code': _('کدپستی')
        }

        validators = {
            'email' : EmailValidator('ایمیل وارد شده معتبر نمیباشد')
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('ایمیل وارد شده تکراری میباشد')


        return email

    def clean_password(self):

        try:
            password_validation.validate_password(self.cleaned_data.get("password"), self.instance)
        except ValidationError as error:
            raise forms.ValidationError("""
                                        1-این پسورد خیلی کوتاه است حداقل 8 کاراکتر
                                        2-پسورد خیلی ساده است
                                        3-پسورد فقط عدد است
                                        """)

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return password




    def save(self, commit: bool = ...) :
        self.instance.set_password(self.cleaned_data.get("password"))
        return super().save(commit=commit)



class LoginForm(forms.Form):
        email=forms.EmailField(widget=EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید', 'type':'email', 'required':'', 'class':'e-field-inner'}),label='ایمیل')
        password=forms.CharField(max_length=16,widget=PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'type':'password', 'required':'', 'class':'e-field-inner'}),label='رمزعبور')

        
        fields = ['email','password']



        labels = {
            'email' : 'ایمیل',
            'password' : 'کلمه عبور',
        }

class ForgetPasswordForm(forms.Form):
            email=forms.EmailField(widget=EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید', 'type':'email', 'required':'', 'class':'e-field-inner'}),label='ایمیل  ')
            

            
            fields = ['email']



            labels = {
                'email' : _('ایمیل'),
            }

class ForgetPassForm(forms.Form):
        password=forms.CharField(max_length=16,widget=PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'type':'password', 'required':'', 'class':'e-field-inner'}),label=' رمزعبور')
        re_password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را تکرار نمایید', 'type':'password', 'required':'', 'class':'e-field-inner'}),label='تکرار رمزعبور')



        
        fields = ['password',"re_password"]

        widgets = {

            'password': PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'type':'password', 'required':'', 'class':'e-field-inner', "id":"password"}),

        }

        labels = {

            'password' : _('رمزعبور'),
            're_password' :'تکرار رمزعبور',

        }

        validators = {
            
        }
    

        def clean_re_password(self):
            password = self.cleaned_data.get('password')
            re_password = self.cleaned_data.get('re_password')


            if password != re_password:
                raise forms.ValidationError('کلمه های عبور مغایرت دارند')

            return password

        def save(self, commit: bool = ...) :
            self.instance.set_password(self.cleaned_data.get("password"))
            return super().save(commit=commit)
