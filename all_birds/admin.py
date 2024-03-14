from django.contrib import admin
from .models import Bird, BirdSaw


@admin.register(Bird)
class BirdAdmin(admin.ModelAdmin):
    list_display = ['name', 'feather_color', 'image']
    search_fields = ['name', 'feather_color']


@admin.register(BirdSaw)
class BirdSawAdmin(admin.ModelAdmin):
    list_display = ['bird', 'saw']
    list_filter = ['saw']
