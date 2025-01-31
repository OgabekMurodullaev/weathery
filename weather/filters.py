import django_filters
from django_filters import FilterSet
from rest_framework.exceptions import ValidationError

from .models import Weather


class WeatherFilter(FilterSet):
    country = django_filters.CharFilter(method='filter_countries')
    id = django_filters.NumberFilter(field_name='id', lookup_expr='exact')

    class Meta:
        model = Weather
        fields = ['country', 'id']

    def filter_countries(self, queryset, name, value):
        countries = value.split(', ')

        invalid_countries = [country for country in countries if not Weather.objects.filter(country_name=country).exists()]

        if invalid_countries:
            raise ValidationError(f"Country(ies) not found: {', '.join(invalid_countries)}")
        return queryset.filter(country_name__in=countries)