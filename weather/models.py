from django.db import models
from .functions import get_temperature_color, get_wind_color, get_cloud_color

class Weather(models.Model):
    city_name = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    temperature = models.FloatField()
    wind_speed = models.FloatField()
    cloud_cover = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    temp_color = models.CharField(max_length=7, blank=True)
    wind_color = models.CharField(max_length=7, blank=True)
    cloud_color = models.CharField(max_length=7, blank=True)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        self.temp_color = get_temperature_color(temperature=self.temperature)
        self.wind_color = get_wind_color(wind_speed=self.wind_speed)
        self.cloud_color = get_cloud_color(cloud_coverage=self.cloud_cover)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.city_name}, {self.country_name}"
