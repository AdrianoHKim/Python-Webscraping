import urllib.request, urllib.parse, urllib.error
import json

# If there is an API key or not
api_key = False

# Verifying API key
if api_key is False:
    api_key = 42  # Default key, if there is no specific one
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'  # Service URL without API key
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'  # Service URL with API key

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address, 'key': api_key})  # Construct the URL with the location and API key

    print('Retrieving', url)  # Display the requested URL
    uh = urllib.request.urlopen(url)  # Display the request URL
    data = uh.read().decode()  # Read the returned data and decode it to string
    print('Retrieved', len(data), 'characters')  # Displays the number of characters received

    try:
        js = json.loads(data)  # Try to interpret JSON data
    except:
        js = None  # If there is an error, set js to None

    if not js or 'status' not in js or js['status'] != 'OK':  # Check if the response is successful
        print('==== Failure To Retrieve ====')
        print(data)  # In case of failure, display the raw data
        continue

    place_id = js['results'][0]['place_id'] # Get the place_id of the first result
    print('Place id', place_id)  # Display the place_id
