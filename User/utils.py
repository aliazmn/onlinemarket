from django.db.models import Q

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



