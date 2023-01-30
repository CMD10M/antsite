from django.contrib import admin
from .models import IntegerPair

@admin.register(IntegerPair)
class IntegerPairAdmin(admin.ModelAdmin):
    list_display = ('hour', 'load')