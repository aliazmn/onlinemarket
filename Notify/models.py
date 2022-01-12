from django.db import models
from User.models import Customer
from Product.models import Product
from django.utils.translation import gettext as _



class notif_user(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="notiftocustomer")
    product=models.ManyToManyField(Product)
    image_notif =models.ImageField(upload_to="Notification/notif_user",null=True, blank=True, help_text="تصویر خود را آپلود کنید ",verbose_name=_('image'))
    file_notif=models.FileField(upload_to="Notification/notif_user",null=True, blank=True, help_text="فایل خود را آپلود کنید ",verbose_name=_('file'))
    text_notif=models.TextField(verbose_name=_('Text'),help_text="توضیحات مربوطه")

    class Meta:
        verbose_name = "notif_user"
        verbose_name_plural ="notif_users"

    def __str__(self) -> str:
        return self.user.profile.first_name

class News(models.Model):
    image_news =models.ImageField(upload_to="Notification/News",null=True, blank=True, help_text="تصویر خود را آپلود کنید ",verbose_name=_('image'))
    file_news=models.FileField(upload_to="Notification/News",null=True, blank=True, help_text="فایل خود را آپلود کنید ",verbose_name=_('file'))
    text_new=models.TextField(verbose_name=_('Text'),help_text="توضیحات مربوطه")

    class Meta:
        verbose_name = "News"

    def __str__(self) -> str:
        return str(self.id)

    