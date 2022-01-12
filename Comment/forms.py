from django.forms.models import ModelForm
from django.forms.widgets import EmailInput, PasswordInput, TextInput, Textarea
from .models import CommentMe
from django import forms


class CommentForm(ModelForm):

    


    email=forms.EmailField(widget=EmailInput(attrs={'placeholder': 'ایمیل شما', 'type':"email", 'class':"e-field-inner",'label':"ایمیل خود را وارد کنید "}))     
    class Meta:
        model = CommentMe
        fields = ('email','comment')

        help_texts={
            "comment":""
        }

        labels = {
            "email": "ایمیل",
            "comment":"کامنت"
        }
        widgets = {
                
                'comment':Textarea(attrs={"class":"e-field-inner",'placeholder':"کامنت شما"})
        }
    
    