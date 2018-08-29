from django.contrib import admin

# Register your models here.

from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name','age','sex'] # customize what all to be displayed on admin screen list
