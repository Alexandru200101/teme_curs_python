from django.contrib import admin
from .models import Firma

@admin.register(Firma)
class FirmaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nume', 'user')






