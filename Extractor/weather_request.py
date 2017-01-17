import json
import requests
import random


# api key to access the weather data


class GetWeatherInfo(object):

	def __init__(self,cityName):
		self.cityName = cityName
		self.weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&APPID={1}'
		self.API_Key = '396cbf110cc7bd1bd3087f317643a83f'
		try:
			# send a request to the page and get the page
			self.requested_page = requests.get(self.weather_url.format(self.cityName,self.API_Key))
			#print('Sending request')
			#convert the page data into  json data

			self.json_data = json.loads(self.requested_page.text)
			#print(self.json_data)
		except Exception as e:
			print(e)

	def Convert_temp(self,temp,unit):
		self.temp = temp
		self.unit = unit
		# the unit is just to convert and return between temperature units
		# c : identifies temperature units in celsius
		# f : in fahrenite
		if self.unit == 'c':
			self.temp -=273
			return self.temp



	def Get_temperature(self):
		try:
			# tempterature
			self.cityTemp = self.json_data['main']['temp_max']
			# just to calculate the avg_temp
			self.Maxtemp = float(self.json_data['main']['temp_max'])
			self.Mintemp = float(self.json_data['main']['temp_min'])
			# gets the average temperature of the city
			self.Avg_temp = (self.Maxtemp + self.Mintemp)/2.0
		except Exception:
			raise Exception("Something went wrong!")

		# returns 2 values : temperature in Celsius and average temperature
		return [self.Convert_temp(self.cityTemp,'c'),self.Avg_temp]

	def Get_weather(self):
		#print('Collecting weather data...')
		# returns the type of weather, pressure, humidity, wind speed

		# getting weather
		self.cityWeather = self.json_data['weather'][0]['main']
		self.cityWeather_discription = self.json_data['weather'][0]['description']

		# getting pressure, wind and humidity
		self.city_pressure = self.json_data['main']['pressure']
		self.city_humidity = self.json_data['main']['humidity']
		self.city_wind = self.json_data['wind']['speed']
		# returns weather, description, pressure and humidity, wind
		return [self.cityWeather,self.cityWeather_discription,self.city_pressure,self.city_humidity,self.city_wind]

	def Get_other_information(self):
		self.CityName1 = self.json_data['name'] # returns the city name
		self.Country_Abs = self.json_data['sys']['country'] # returns the abrivated country name
		# returns a list having cityName1 and country_Abs
		return [self.CityName1,self.Country_Abs]


	def Get_coords(self):
		self.lat = self.json_data['coord']['lat']
		self.lon = self.json_data['coord']['lon']
		return self.lat,self.lon
