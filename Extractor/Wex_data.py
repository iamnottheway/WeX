
import Wex_request

def ConvertTemperature(temp,unit='cel'):
	'''
	Converts to any unit based on the unit parameter
	defalut unit is celcius.

	if the parameter is not specified, it is converted to celcius.

	To convert to farhenite, suply 'far' as the second argument 

	'''
	#converts to celcius
	temp -= 273
	if temp is '':
		return None
	
	if unit is 'cel':
		# converts to celcius
		return round(temp,2)
	else:
		if unit is 'far':
			return round((temp*(9/5)+32),2)
		else:
			print("Use a proper convertion unit : 'cel' for Celcius and 'far' farhenite")


class GetWeatherConditions(object):

	def __init__(self,CityName,ApiKey):

		self.CityName = CityName
		self.ApiKey = ApiKey
		self.WeatherObject = Wex_request.WexExtractor(self.CityName,self.ApiKey)
		self.WeatherDataObject = self.WeatherObject.GetJsonData()
		

	def GetCurrentTemperature(self,unit='cel'):
		'''
			returns the current temperature of London

			The argument unit, specifies the convertion unit.
			Celcius is the defalut unit, if you don't know what to
			do, don't pass the  argument. And if you  know 
			what to do, then suply 'far' as the  argument to
			convert to fahrenite.

		'''
		return ConvertTemperature(self.WeatherDataObject['main']['temp_max'],unit)

	def GetCurrentHumidity(self):
		''' returns the current humidity'''
		return self.WeatherDataObject['main']['humidity']

	def GetCurrentPressure(self):
		''' returns the current pressure in the city'''
		return self.WeatherDataObject['main']['pressure']

	def GetCurrentCoords(self):
		''' returns the coordinates of the place in a tuble. tuple[0] --> lat and tuple[1] --> lon'''
		return (self.WeatherDataObject['coord']['lat'],self.WeatherDataObject['coord']['lon'])

	def GetCurrentWeather(self):
		''' returns the current weather in a tuple. tuple[0] --> current phenomenon and tuple[1] --> weather description'''
		return (self.WeatherDataObject['weather'][0]['main'],self.WeatherDataObject['weather'][0]['description'])

	def GetCloudCoverPercent(self):
		''' returns the percentage of clouds covering a particular place. Should be denoted in percentage'''
		return self.WeatherDataObject['clouds']['all']

if __name__ == '__main__':
	WeXdata =GetWeatherConditions("London","[API_KEY]")
	print(WeXdata.GetCurrentTemperature())
	print(WeXdata.GetCurrentHumidity())
	print(WeXdata.GetCurrentCoords())
	print(WeXdata.GetCurrentWeather())
	print(WeXdata.GetCloudCoverPercent())