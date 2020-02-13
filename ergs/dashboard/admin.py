from django.contrib import admin
# from leaflet.admin import LeafletGeoAdmin
# Register your models here.
from .models import *


admin.site.register(all_available_card)
admin.site.register(user_data)
admin.site.register(machine_on_bus_station)
admin.site.register(bus_station)
admin.site.register(exit_log)
admin.site.register(entry_log)
admin.site.register(recharge_log)
admin.site.register(vendor_data)
admin.site.register(fare_collection)
admin.site.register(recharge)
