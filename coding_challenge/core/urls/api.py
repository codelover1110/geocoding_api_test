from django.urls import path
from coding_challenge.core.views import (
    GetGeocodeView,
    ReverseGeocodeView,
    CalculateGeometricDistanceView,
)


urlpatterns = [
    path('getGeocode/', GetGeocodeView.as_view()),
    path('reverseGeocode/', ReverseGeocodeView.as_view()),
    path('calculateGeometricDistance/', CalculateGeometricDistanceView.as_view()),
]