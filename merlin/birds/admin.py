from django.contrib import admin
from .models import Order, Event, Family, Genus, Location, Species

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_filter = ['name',]
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_filter = ['name',]
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


@admin.register(Genus)
class GenusAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_filter = ['name',]
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ['common_name', 'species', 'link']
    list_filter = ['common_name',]
    search_fields = ['common_name', 'species']
    prepopulated_fields = {'slug': ('common_name',)}
    ordering = ['common_name']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug' : ('name',)}
    ordering = ['name']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['location', 'date']
    list_filter = ['location', 'date']
    search_fields = ['location', 'date']
    prepopulated_fields = {'slug': ('date',)}
    ordering = ['-date', 'location']
