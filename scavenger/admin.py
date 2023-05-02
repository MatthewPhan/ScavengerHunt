from django.contrib import admin
from scavenger.models import Location, Event

# Location Model for QR Generator 
admin.site.register(Location)

admin.site.register(Event)