from django.db import models

from User.models import Profile


class Payment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='کاربر مربوطه')
    
    order_id = models.TextField(null=True)
    payment_id = models.TextField(null=True)
    amount = models.IntegerField(null=True)
    date = models.TextField(default='-')
    card_number = models.TextField(default="****")
    idpay_track_id = models.IntegerField(default=0000)
    bank_track_id = models.TextField(default=0000)
    status = models.IntegerField(default=0)
    
    
    

    def __str__(self):
        return self.user.email