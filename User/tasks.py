from celery import shared_task
from .utils import Send_email


@shared_task()
def my_validate(to_email,uid,opt):
    Send_email(to_email,uid,opt)