#NOTE: replace YOUR-API-KEY with your api key 

import json
from urllib.request import urlopen

main_api = 'https://maps.googleapis.com/maps/api/geocode/json?'
apikey = 'YOUR-API-KEY'
address = 'lhr'

with urlopen('https://maps.googleapis.com/maps/api/geocode/json?address=lhr&key=YOUR-API-KEY') as response:
  output = response.read()

#print(output)
data = json.loads(output)

json_status = data['status']
print('API status: '+ json_status)

formatted_address = data['results'][0]['formatted_address']
print(formatted_address)

more_dtl = data['results'][0]['address_components'][0]['types'][0]
print(more_dtl)


# The sample invokation on web browser
# https://maps.googleapis.com/maps/api/geocode/json?address=YOUR-API-KEY-HERE
