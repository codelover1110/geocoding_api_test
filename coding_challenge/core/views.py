from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
import googlemaps
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter, extend_schema_view, inline_serializer
from rest_framework.response import Response
import geopy.distance
from coding_challenge.core.models import Geocode
from coding_challenge.core.serializers import GeoCodeSerializer
from django.db.models import Q

gmaps = googlemaps.Client(key=settings.GOOGLE_MAP_API_KEY)


# Geocoding an address
class GetGeocodeView(APIView):

  @extend_schema(
    description="""Geocoding an address""",
    parameters=[
        OpenApiParameter(name='address', required=True, type=str, description='Geocoding an address'),
    ],
    responses={
        200: OpenApiResponse('The geometry location with latitude and longitude togheter with corressponding formatted address'),
        400: OpenApiResponse(description='Malformed request'),
    }
  )
  def post(self, request, format=None):
    try:
      address =request.data.get('address')
      # check if address is already in database
      # we're using .first() to retrieve only the first matching record. This is efficient because we only need one result.
      geocode = GeoCode.object.filter(address=address).first()
      if geocode is None:
        geocode_result = gmaps.geocode(address)

        return_geocode = None
        # store all geo code returned from api
        for geocode_result_item in geocode_result:
          geocode_in_loop = GeoCode.object.filter(address=address).first()
          if geocode_in_loop is None:
            geocode_in_loop = Geocode.objects.create(
              formatted_address=geocode_result_item['formatted_address'],
              lat=geocode_result_item['geometry']['location']['lat'],
              lng=geocode_result_item['geometry']['location']['lng'],
            )
          if return_geocode is None:
            return_geocode = geocode_in_loop

        return Response(data=GeoCodeSerializer(return_geocode).data, status=status.HTTP_200_OK)
      else:
        return Response(data=GeoCodeSerializer(geocode).data, status=status.HTTP_200_OK)
    except Exception as e:
      return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Look up an address with reverse geocoding
class ReverseGeocodeView(APIView):
  @extend_schema(
    description="""Look up an address with reverse geocoding""",
    parameters=[
        OpenApiParameter(name='lat', required=True, type=str, description='Geometry location latitude'),
        OpenApiParameter(name='lng', required=True, type=str, description='Geometry location longitude'),
    ],
    responses={
        200: OpenApiResponse('The formatted address with the given geometry in latitude and longitude'),
        400: OpenApiResponse(description='Malformed request'),
    }
  )
  def post(self, request, format=None):
    try:
      lat =request.data.get('lat')
      lng =request.data.get('lng')

      # check if address is already in database
      # we're using .first() to retrieve only the first matching record. This is efficient because we only need one result.
      geocode = GeoCode.object.filter(Q(lat=lat) & Q(lng=lng)).first()
      if geocode is None:
        reverse_geocode_result = gmaps.reverse_geocode((lat, lng))
        data = []
        for reverse_geocode_result_item in reverse_geocode_result:
          lat = reverse_geocode_result_item['geometry']['location']['lat']
          lng = reverse_geocode_result_item['geometry']['location']['lng']
          geocode_in_loop = GeoCode.object.filter(Q(lat=lat) & Q(lng=lng)).first()
          if geocode_in_loop is None:
            geocode_in_loop = Geocode.objects.create(
              formatted_address=reverse_geocode_result_item['formatted_address'],
              lat=lat,
              lng=lng,
            )
          if return_geocode is None:
            return_geocode = geocode_in_loop

        return Response(data=GeoCodeSerializer(return_geocode).data, status=status.HTTP_200_OK)
      else:
        return Response(data=GeoCodeSerializer(geocode).data, status=status.HTTP_200_OK)
    except Exception as e:
      return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CalculateGeometricDistanceView(APIView):
  @extend_schema(
    description="""Calculates the geometric distance in units of your choice between two lat/long coordinates, and return the distance""",
    parameters=[
        OpenApiParameter(name='lat_1', required=True, type=str, description='Latitude of coordinate 1'),
        OpenApiParameter(name='lng_1', required=True, type=str, description='Longitude of coordinate 1'),
        OpenApiParameter(name='lat_2', required=True, type=str, description='Latitude of coordinate 2'),
        OpenApiParameter(name='lng_2', required=True, type=str, description='Longitude of coordinate 2'),
    ],
    responses={
        200: OpenApiResponse('The distance between coordinate (lat_1, lng_1) and coordinate (lat_2, lng_2)'),
        400: OpenApiResponse(description='Malformed request'),
    }
  )
  def post(self, request, format=None):
    try:
      lat_1 = request.data.get('lat_1')
      lng_1 = request.data.get('lng_1')
      lat_2 = request.data.get('lat_2')
      lng_2 = request.data.get('lng_2')
      start_address = request.data.get('start_address')
      destination_address = request.data.get('destination_address')

      if start_address and destination_address:
        # Make Google Maps API request to get distance details
        directions_result = gmaps.directions(start_address, destination_address, mode="driving")

        if not directions_result:
            return Response({'error': 'Unable to calculate distance.'}, status=500)

        # Extract distance from the API response
        distance = directions_result[0]['legs'][0]['distance']['text']

        return Response({'distance': distance}, status=200)
      
      elif lat_1 and lng_1 and lat_2 and lng_2:
        coords_1 = (lat_1, lng_1)
        coords_2 = (lat_2, lng_2)

        # Make Google Maps API request to get distance details
        distance = geopy.distance.geodesic(coords_1, coords_2)

        data = {
          'distance_km': distance.km,
          'distance_m': distance.m,
          'distance_miles': distance.miles,
        }
        return Response(data=data, status=status.HTTP_200_OK)
      
      else:
        return Response({'error': 'Both start and destination addresses are required.'}, status=400)
      
    except Exception as e:
      return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
