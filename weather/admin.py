from django.contrib import admin

from weather.models import Weather

class WeatherAdmin(admin.ModelAdmin):
    list_display = ["id", "city_name", "country_name", "timestamp"]
    ordering = ["id"]


admin.site.register(Weather, WeatherAdmin)
