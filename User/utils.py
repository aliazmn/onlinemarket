from django.db.models import Q
from django.core.cache import caches
from User.models import UserDevice

from django.core.mail import send_mail
from django.core.cache import cache
from django.urls import reverse

from uuid import uuid4
from project import settings

#--------------------------send mail for forget password and activate link-----------------------
def Send_email(to_email,uid,opt):
    if opt == "activate":
        
        link=reverse("user:activate",kwargs={"valid":uid})
    elif opt == "forget-pass":
        
        link=reverse("user:set_true",kwargs={"auten":uid})
        
    mail_subject = 'click on link for continue'
    if settings.DEBUG :
        
        message = "127.0.0.1:8000"+link
    else :
        message = "217.182.230.17:8001"+link
        
    # request.session["email"]=to_email
    # request.session["uid"]=uid
    # cache.set(to_email,uid,180)
    print(message)
    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])

def make_session (request,to_email):
    uid=str(uuid4())
    request.session["email"]=to_email
    request.session["uid"]=uid
    cache.set(to_email,uid,180)
    return uid

def linked_devices(request,user):
    if request.user_agent.is_mobile:
        device = "Mobile"
    if request.user_agent.is_tablet:
        device = "Tablet"
    if request.user_agent.is_pc:
        device = "PC"
    browser=request.user_agent.browser.family
    os=request.user_agent.os.family
    query=UserDevice.objects.filter(Q(user=user)&Q(device=device)&Q(browser=browser))
    if not query:
        UserDevice.objects.create(user=user,device=device,browser=browser,os=os)







def filling_cart(request):
    if not request.session.session_key:
        request.session.save()
    redis_cache=caches['default']
    cart=redis_cache.client.get_client()
    carts=cart.hgetall(request.session.session_key)
    for elm in carts:
        cart.hset(request.user.email,elm.decode("utf-8"),carts[elm])
