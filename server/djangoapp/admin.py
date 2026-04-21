from django.contrib import admin
from .models import CarMake, CarModel


class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 3


class CarModelAdmin(admin.ModelAdmin):
    list_display = ['car_make', 'name', 'car_type', 'year', 'dealer_id']
    list_filter = ['car_type', 'year', 'car_make']
    search_fields = ['name']


class CarMakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'country_of_origin', 'founded_year']
    inlines = [CarModelInline]
    search_fields = ['name']


admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
