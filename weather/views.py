from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from weather.filters import WeatherFilter
from weather.models import Weather
from weather.serializers import WeatherListSerializer


class WeatherListView(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Weather.objects.all()
    serializer_class = WeatherListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = WeatherFilter