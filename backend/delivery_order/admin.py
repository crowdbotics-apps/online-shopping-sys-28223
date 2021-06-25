from django.contrib import admin
from .models import Order, PaymentMethod, Bill

admin.site.register(Bill)
admin.site.register(PaymentMethod)
admin.site.register(Order)

# Register your models here.
