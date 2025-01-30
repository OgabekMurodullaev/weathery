from django.db import models


class Weather(models.Model):
    city_name = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    temperature = models.FloatField()
    wind_speed = models.FloatField()
    cloud_cover = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager



    def __str__(self):
        return f"{self.city_name}, {self.country_name}"
