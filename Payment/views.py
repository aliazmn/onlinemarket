import os
import uuid
from django.shortcuts import render, redirect,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , get_user_model

from Cart.models import History


from idpay.api import IDPayAPI
from .models import Payment

from .utils import create_factor

User = get_user_model()


def payment_init():
    base_url = os.environ.get('BASE_URL')
    api_key = os.environ.get('MERCHANT_CODE')
    sandbox = os.environ.get('IDPAY_SANDBOX')

    return IDPayAPI(api_key, base_url, bool(sandbox))

@login_required(login_url="/user/login/")
def payment_start(request,amount):
    if request.method == 'GET':

        order_id = uuid.uuid1()


        payer = {
            'name': request.user.first_name,
            'mail': request.user.email,
        }

        record = Payment(user=request.user, order_id=order_id, amount=int(amount))
        record.save()

        idpay_payment = payment_init()
        result = idpay_payment.payment(str(order_id), amount, 'payment/payment-return/', payer)
        if 'id' in result:
            record.status = 1
            record.payment_id = result['id']
            record.save()

            return redirect(result['link'])

        else:
            txt = result['message']
    else:
        txt = "Bad Request"

    return JsonResponse({"text":txt})


@csrf_exempt
def payment_return(request):
    if request.method == 'POST':

        
        pid = request.POST.get('id')
        status = request.POST.get('status')
        pidtrack = request.POST.get('track_id')
        order_id = request.POST.get('order_id')
        amount = request.POST.get('amount')
        card = request.POST.get('card_no')
        date = request.POST.get('date')

        payment_obj=Payment.objects.filter(order_id=order_id, payment_id=pid, amount=amount, status=1)
        if payment_obj.count() == 1:


            login(request,payment_obj[0].user)

            idpay_payment = payment_init()

            payment = Payment.objects.get(payment_id=pid, amount=amount)
            payment.status = status
            payment.date = str(date)
            payment.card_number = card
            payment.idpay_track_id = pidtrack
            payment.save()

            if str(status) == '10':

                
                result = idpay_payment.verify(pid, payment.order_id)

                if 'status' in result:

                    
                    payment.status = result['status']
                    payment.bank_track_id = result['payment']['track_id']
                    payment.save()

                    if result['status'] == 100:

                        
                        create_factor(request,pidtrack)


                    return redirect("home")

                else:
                    txt = result['message']

            else:
                txt = "Error Code : " + str(status) + "   |   " + "Description : " + idpay_payment.get_status(status)

        else:
            txt = "Order Not Found"

    else:
        txt = "Bad Request"

    return JsonResponse({"text":txt})

  
def show_factors(request):
    history=History.objects.filter(customer=request.user)
    ctx,counter={},1
    for elm in history:
        ctx[f"factor{counter} in date {elm.date}"]=elm.factor
        
        
    return JsonResponse(ctx)


