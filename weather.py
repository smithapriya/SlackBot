import requests
import pytemperature

api_url = 'http://api.openweathermap.org/data/2.5/weather?id=5327684&APPID=d8cca210b4330a8ab107b05b20b66d58'
api_weather = requests.get(url=api_url)
#current_weather = requests.get('api.openweathermap.org/data/2.5/weather?lat=37&lon=122')
weather = api_weather.json()

temp_current = pytemperature.k2f(weather['main']['temp'])
temp_min = pytemperature.k2f(weather['main']['temp_min'])
temp_max = pytemperature.k2f(weather['main']['temp_max'])
location = weather['name']
adjective = str(weather['weather'][0]['description']) + 'y'
print(adjective)

def current_weather():
	message = 'The current weather in ' + str(location) + ' is ' + adjective + ' and currently ' + str(temp_current) + '°F with a high of ' + str(temp_max) + '°F and a low of ' + str(temp_min) + '°F'
	return message


{'coord': {'lon': -122.27, 'lat': 37.87}, 
'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50n'}], 
'base': 'stations', 
'main': {'temp': 286.4, 'pressure': 1017, 'humidity': 93, 'temp_min': 284.15, 'temp_max': 290.15}, 
'visibility': 14484, 
'wind': {'speed': 5.1, 'deg': 310}, 
'clouds': {'all': 20}, 
'dt': 1524549600, 
'sys': {'type': 1, 'id': 439, 'message': 0.0079, 'country': 'US', 'sunrise': 1524576073, 'sunset': 1524624817}, 
'id': 5327684, 
'name': 'Berkeley', 
'cod': 200}