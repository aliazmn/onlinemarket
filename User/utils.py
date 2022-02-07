
from django.core.mail import send_mail
from django.core.cache import cache
from django.urls import reverse

from uuid import uuid4
from project import settings

#--------------------------send mail for forget password and activate link-----------------------
def Send_email(request,to_email,opt):
    if opt == "activate":
        uid=str(uuid4())
        link=reverse("user:activate",kwargs={"valid":uid})
    elif opt == "forget-pass":
        uid=str(uuid4())
        link=reverse("user:set_true",kwargs={"auten":uid})
        
    mail_subject = 'click on link for continue'
    message = "127.0.0.1:8000"+link
    request.session["email"]=to_email
    request.session["uid"]=uid
    cache.set(to_email,uid,180)
    print("<<<-------------------------------------------------------------------->>>")
    print(message)
    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])