from django.contrib import admin
from .models import Plant, Station, Demand, Function, Layout, PlantResult
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Station
    extra = 10

class PlantAdmin(admin.ModelAdmin):
    fields = ['plant_name']
    inlines = [ChoiceInline]

class ResultsInline(admin.TabularInline):
    model = PlantResult
    extra = 0

class LayoutAdmin(admin.ModelAdmin):
    fields = ['layout_name']
    inlines = [ResultsInline]

admin.site.register(Plant, PlantAdmin)
admin.site.register(Station)
admin.site.register(Demand)
admin.site.register(Function)
admin.site.register(Layout, LayoutAdmin)
admin.site.register(PlantResult)

# admin.site.register(Plant)
# admin.site.register(Station)
