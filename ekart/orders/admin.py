from django.contrib import admin
from orders.models import OrderedItems, Orders 
# Register your models here.

admin.site.register(OrderedItems)
admin.site.register(Orders)