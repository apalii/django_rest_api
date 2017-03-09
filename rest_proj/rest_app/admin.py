from django.contrib import admin

from .models import Customer, Appliance, Status

admin.site.register(Customer)
admin.site.register(Appliance)
admin.site.register(Status)
