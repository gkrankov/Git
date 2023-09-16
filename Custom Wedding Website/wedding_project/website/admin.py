from django.contrib import admin
from .models import Couple

@admin.register(Couple)
class CoupleAdmin(admin.ModelAdmin):
    list_display = ('bride_name', 'groom_name', 'wedding_date', 'contact_email')

