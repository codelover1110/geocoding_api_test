from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.response import Response
import json

class GoogleMapApiTestCase(APITestCase):
    def setUp(self):
      pass

    def test_get_geocode(self):
      response = self.client.post(
        f'/api/getGeocode/',
        json.dumps(dict(address='1600 Amphitheatre Parkway, Mountain View, CA')),
        content_type='application/json',
      )
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertFalse(response.data is None)
      self.assertTrue('formatted_address' in response.data)
      self.assertTrue('lat' in response.data)
      self.assertTrue('lng' in response.data)


    def test_reverse_geocode(self):
      response = self.client.post(
        f'/api/reverseGeocode/',
        json.dumps(dict(lat='37.4223928', lng='-122.0841883')),
        content_type='application/json',
      )
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertFalse(response.data is None)
      self.assertTrue('formatted_address' in response.data)
      self.assertTrue('lat' in response.data)
      self.assertTrue('lng' in response.data)


    def test_calculate_geometric_distance(self):
      response = self.client.post(
        f'/api/calculateGeometricDistance/',
        json.dumps(dict(lat_1='37.4223928', lng_1='-122.0841883', lat_2='17.4223928', lng_2='-132.0841883')),
        content_type='application/json',
      )
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertFalse(response.data is None)
      self.assertTrue('distance_km' in response.data)
      self.assertTrue('distance_m' in response.data)
      self.assertTrue('distance_miles' in response.data)

