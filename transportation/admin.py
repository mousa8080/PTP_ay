from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Wallet)
admin.site.register(Vehicle)
admin.site.register(Route)
admin.site.register(Ticket)
admin.site.register(Transaction)
admin.site.register(VehicleTracking)
admin.site.register(DriverEarnings)
admin.site.register(Report)