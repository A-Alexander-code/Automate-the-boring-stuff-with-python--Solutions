# python
# getOpenWeather.py - Prints the weather for a location from the command line.

APPID = 'YPUR_APPID_HERE'

import json, requests, sys

# Compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

# TODO: Download the JSON data from OpenWeatherMap.org's API.
url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' % (location,APPID)
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
print(response.txt)

# TODO: Load JSON data into a Python variable
weatherData =  json.loads(response.txt)

# Print weather descriptions
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][1]['main'],'-',w[1]['weather'][1]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][2]['main'],'-',w[2]['weather'][2]['description'])