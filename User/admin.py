from django.contrib import admin

# Register your models here.
from .models import Profile,Admin,Customer,SalesMan



admin.site.register(Profile)
admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(SalesMan)
