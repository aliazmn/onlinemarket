from django.db.models import Q
from django.core.cache import caches
from User.models import UserDevice

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
