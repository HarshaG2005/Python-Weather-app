import requests
import json
api='ed8585fee9ea4e524bbf1493452439eb'
ct="Negombo"

params={ 'q':ct,
        'appid':api,
       'units':'metric'
       }
try:
 response=requests.get('http://api.openweathermap.org/data/2.5/weather',params=params)
 response.raise_for_status()
 weatherdata=response.json()
 print(weatherdata)
except:
 print('error')
