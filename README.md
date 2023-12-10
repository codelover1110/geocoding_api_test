Site test url: http://149.28.86.112:8000/

I) Change the Google Map API key to your key at /coding_challenge/settings.py

GOOGLE_MAP_API_KEY = 'AIzaSyBIgOmdnklqb-xOCNLb1A8Hb9ju911KO0M'

II) Endpoints

1) /api/getGeocode/
Method: POST
Description: get geocoding for an address
Params:
    + address: Geocoding an address

HTTP status:
    200: The geometry location with latitude and longitude togheter with corressponding formatted address
    400: Malformed request

Format Output:
    {'formatted_address': <address with formated string>, 'lat': <latitude number>, 'lng': <longitude number>}


2) /api/reverseGeocode/
Method: POST
Description: Look up an address with reverse geocoding
Params:
    + lat: Geometry location latitude
    + lng: Geometry location longitude

HTTP status:
    200: The formatted address with the given geometry in latitude and longitude
    400: Malformed request

Format Output:
    {'formatted_address': <address with formated string>, 'lat': <latitude number>, 'lng': <longitude number>}

3) /api/calculateGeometricDistance/
Method: POST
Description: Calculates the geometric distance in units of your choice between two lat/long coordinates, and return the distance
Params:
    + lat_1: Latitude of coordinate 1
    + lng_1: Longitude of coordinate 1
    + lat_2: Latitude of coordinate 2
    + lng_2: Longitude of coordinate 2

HTTP status:
    200: The distance between coordinate (lat_1, lng_1) and coordinate (lat_2, lng_2)
    400: Malformed request

Format Output:
    {'distance_km': <distance in km unit>,
    'distance_m': <distance in metter unit>,
    'distance_miles': <distance in miles unit>}