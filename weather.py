import requests
import json
n=input("City:")
api='ed8585fee9ea4e524bbf1493452439eb'
ct=n

params={ 'q':ct,
        'appid':api,
       'units':'metric'
       }
try:
 response=requests.get('http://api.openweathermap.org/data/2.5/weather',params=params)
 response.raise_for_status()
 weatherdata=response.json()


except requests.exceptions.RequestException as e:
    print(f"Error during the HTTP request: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON response: {e}")
    print(f"Raw response text: {response.text}")  # Print the raw response for debugging
except Exception as e:  # Catch any other unexpected exceptions
    print(f"An unexpected error occurred: {e}")
city_name=weatherdata.get('name')
country_code=weatherdata.get('sys',{}).get('country')
description=weatherdata.get('weather',[{}])[0].get('description')
temprature=weatherdata.get('main',{}).get('temp')
feels_like=weatherdata.get('main',{}).get('feels_like')
humiditiy=weatherdata.get('main',{}).get('humidity')
wind_speed=weatherdata.get('wind',{}).get('speed')
sunrise_timeS=weatherdata.get('sys',{}).get('sunrise')
sunset_timeS=weatherdata.get('sys',{}).get('sunset')
import datetime
time_offset_seconds=weatherdata.get('timezone',0)
time_offset=datetime.timedelta(time_offset_seconds)
def format_time(timestamp):
    if timestamp:
        dt_object=datetime.datetime.fromtimestamp(timestamp)+time_offset
        return dt_object.strftime('%I:%M %p')
    else:
        return 'N/A'
sunrise_time=format_time(sunrise_timeS)
sunset_time=format_time(sunset_timeS)
weather_report=f"This is the Weather report of the {city_name},{country_code}:\n"
weather_report+=f"Description:{description.capitalize()} \n"
weather_report+=f"temprature:{temprature:.1f}°C(it feels like:{feels_like}°C)\n"
weather_report+=f"Humidity:{humiditiy}\n"
weather_report+=f"Sunrise:{sunrise_time}\n"
weather_report+=f"Sunset:{sunset_time}\n"
weather_report+=f"Windspeed:{wind_speed:.2f}\n"
print(weather_report)

