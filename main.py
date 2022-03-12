# PythonAnywhere related code was added to the cloud version, but this is all of the local code

import requests
from twilio.rest import Client

# actual lat/long
# my_lat = 39.6739066
# my_long = -104.9708924

# lat/long for testing
my_lat = 40.86908855507455
my_long = -74.73802105621988

# if hosting this code in a virtual environment, I would want to use environment variables and hide my api_key,\
# auth_token, and anything that could be connected to my payment details or personal info
api_key = 'f151b0da1957f007c297eca76f342db9'
account_sid = 'AC99fd4a440b59faee41bef12b01daf271'
auth_token = '6f5ccf44acdc189f435f4b162bc1b375'





params = {
    "lat": my_lat,
    "lon": my_long,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()
weather_data = response.json()

# I can also create a "slice" of data by using something like:
# weather_slice = weather_data["hourly"][:12]
# the first part acts as a normal dictionary pull, but then the [:12] indicates we want the first 12 (0 -> 11) of these

forecasted_rain = False

for hour in range(0, 12):
    weather_code = weather_data["hourly"][hour]["weather"][0]['id']
    if weather_code < 700:
        forecasted_rain = True

client = Client(account_sid, auth_token)

if forecasted_rain:
    print("Bring an umbrella!")
    message = client.messages \
        .create(
        body="Bring an umbrella!",
        from_='+12077073712',
        to='+19076026232'
    )
    print(message.status)
else:
    message = client.messages \
        .create(
        body="No rain or snow forecasted in the next 12 hours!",
        from_='+12077073712',
        to='+19076026232'
    )
    print(message.status)