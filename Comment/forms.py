from django.forms.models import ModelForm
from django.forms.widgets import EmailInput, PasswordInput, TextInput, Textarea
from .models import CommentMe
from django import forms


class CommentForm(ModelForm):

    class Meta:
        model = CommentMe
        fields = ('comment',)

        help_texts={
            "comment":""
        }

        labels = {
            "comment":"کامنت"
        }
        widgets = {
                
                'comment':Textarea(attrs={"class":"e-field-inner",'placeholder':"کامنت شما"})
        }
    
    