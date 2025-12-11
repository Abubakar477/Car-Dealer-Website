from django.contrib import admin
from .models import Car
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            '<img src="{}" width="40" style="border-radius: 50px;" />',
            object.car_photo.url
        )
    thumbnail.short_description = 'Car Image'

    list_display = (
        'id', 'thumbnail', 'car_title', 'city', 'color', 'model',
        'year', 'body_style', 'fuel_type', 'is_featured', 'youtube_id'
    )
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type')
    list_filter = ('city', 'model', 'body_style', 'fuel_type')

    fields = (
        'car_title', 'model', 'year', 'price', 'car_photo', 'car_photo_1', 'car_photo_2',
        'car_photo_3', 'car_photo_4', 'youtube_id', 'description', 'city', 'province',
        'color', 'condition', 'body_style', 'engine', 'transmission', 'interior', 'miles',
        'doors', 'passengers', 'vin_no', 'milage', 'fuel_type', 'no_of_owners',
        'features', 'is_featured'
    )

admin.site.register(Car, CarAdmin)
