from django.contrib import admin
from areas.models import Area

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    pass