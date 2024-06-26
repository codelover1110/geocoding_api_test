# Geocoding API Service

Welcome to the Geocoding API service! This service provides endpoints for geocoding and reverse geocoding, as well as calculating geometric distances between coordinates.

### Configuration

Change the Google Map API key to your own key by updating `/coding_challenge/settings.py`.

    ```python
    # /coding_challenge/settings.py
    
    GOOGLE_MAP_API_KEY = 'YOUR_GOOGLE_MAP_API_KEY'
    ```

## Endpoints

### 1. Get Geocode

- **URL:** /api/getGeocode/
- **Method:** POST
- **Description:** Get geocoding for an address
- **Params:**
  - `address`: Geocoding an address
- **HTTP Status:**
  - `200`: The geometry location with latitude and longitude together with the corresponding formatted address
  - `400`: Malformed request
- **Format Output:**
  ```json
  {
    "formatted_address": "",
    "lat": "",
    "lng": ""
  }
![Screenshot](images/getGeocode.png)

### 2. Reverse Geocode

- **URL:** /api/reverseGeocode/
- **Method:** POST
- **Description:** Look up an address with reverse geocoding
- **Params:**
  - `lat`: Geometry location latitude
  - `lng`: Geometry location longitude
- **HTTP Status:**
  - `200`: The formatted address with the given geometry in latitude and longitude
  - `400`: Malformed request
- **Format Output:**
  ```json
  {
    "formatted_address": "",
    "lat": "",
    "lng": ""
  }
![Screenshot](images/reverseGeocode.png)

### 3. Calculate Geometric Distance

- **URL:** /api/calculateGeometricDistance/
- **Method:** POST
- **Description:** Calculates the geometric distance between two lat/long coordinates and returns the distance
- **Params:**
  - `start_address`: The start address
  - `destination_address`: The destination_address
  or
  - `lat_1`: Latitude of coordinate 1
  - `lng_1`: Longitude of coordinate 1
  - `lat_2`: Latitude of coordinate 2
  - `lng_2`: Longitude of coordinate 2
- **HTTP Status:**
  - `200`: The distance between coordinate (lat_1, lng_1) and coordinate (lat_2, lng_2)
  - `400`: Malformed request
- **Format Output:**
   ```json
  {
    "distance": "",
  }

  or

  ```json
  {
    "distance_km": "",
    "distance_m": "",
    "distance_miles": ""
  }
![Screenshot](images/getGeocodeWithaddress.png)

![Screenshot](images/calculateGeometricDistance.png)

### 4. TestCase
![Screenshot](images/testCase.png)

