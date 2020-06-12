step-0: 
documentation link: reference url: https://developers.google.com/maps/documentation/geocoding/start
how to enable apis in gcp, see link below: 
https://www.youtube.com/watch?time_continue=19&v=n1UorU1PALk&feature=emb_logo

how to create api key in gcp, see link below: 
https://www.youtube.com/watch?v=2_HZObVbe-g


step-1: enable the geocoding api in gcp.  search for the text: geocoding and enable it
step-2: search for APIs & Services -> Credentials -> Create Credentials -> API Key  provide key name as myapp-dev-api-key
step-3: add key restrictions to apikey.  find out your ip address from google and mention it in the ip address and click save
step-4: paste the apikey in the invoker python file and run it.
step-5: output given below:

output:
(venv) D:\PK\workspace\python\PycharmProjects\Giraffe>python invoke-google-api.py
API status: OK
Heathrow Airport (LHR), Longford TW6, UK
airport

