

import re
import random
from geotext.geotext import GeoText

class text_processing(object):
	'''

	This class has methods to process the text.
	Methods like uppercase, lowercase, tokenize and sentence parser

	'''
	def __init__(self,text):
		self.text = text


	def getUpperCaps(self):
		return self.text.upper()

	def getLowerCaps(self):
		return self.text.lower()

	def Word_Tokenize(self):
		'''
		Splits the sentence into lower case tokens

		'''
		return self.text.lower().split()



class SearchKeyWords(object):
	
	def __init__(self,string=None):
		self.string = string

	def match_words(self,string):

		'''
		Takes a string as an argument.

		This method matches any keywords like weather, temperature, etcetera.
		if keywords are found, then it returns the keyword

		example :

				>> Whats the weather and temperature in London
				.. ['weather ', 'temperature']


		But when using just use the first element. 
			Ex : list[0]

		Since multiple reading functionality is not added yet

		'''

		# regular exxpression to find or match with the string
		self.regex_match = r"[A-Za-z]eath[a-z]*r |[Tt][Ee][A-Za-z]*p[a-z]*"
		# searches for the regex_match in the string
		self.Matched_keyword = re.findall(self.regex_match,string)
		return self.Matched_keyword

	def KeyWords(self):
		'''

		returns the first keyword from the list
		
		'''
		return self.match_words(self.string)[0]
		


import Wex_data

class WexWeather(object):

	def __init__(self,string,SendRequest=True,Api_Key):

		'''
		
		WexWeather class takes 2 arguments, first one is a string.
		And second argument is a flag variable.

		string : Input anything you want, if there is or there are city
				 names in that string, you'll recieve the city names

		SendRequest: This flag is by default set to true. That means it
					 can send requests to get the weather data. Keep it true
					 if you want to send requests. In anycase you want to 
					 set it to false, do so. It just won't send any request.
					 This is useful if you just want to identify the city names
					 from a string. Setting it to true will also do the same, but
					 sending a request and recieving the data takes some time.

					 Do this only if you want to extract the city names. But if you want 
					 the weather data, set it to true or leave it without passing the 
					 argument.

					 example: with SendRequest=True

							 >> Whats the weather in London and New York and San Jose and San Francisco

								# some seconds later

							.. ['London', 'New York', 'San Jose', 'San Francisco']

					example: with SendRequest=False
							 >> Whats the weather in London and New York and San Jose and San Francisco

								# 0.00000001s later. This is fast!

							.. ['London', 'New York', 'San Jose', 'San Francisco']

			Api_Key : Get your api key from openweather.com and use it.




		'''

		self.Keywords = SearchKeyWords(string)
		# uses GeoText() module to Extract the cities
		self.CityName = GeoText(string).cities
		if SendRequest is True:
			self.WeatherObject = Wex_data.GetWeatherConditions(self.CityName[0],Api_Key)
		else:
			pass


	def WexGetWeather(self):
		self.CityList = self.Keywords.KeyWords() 
		self.CurrentWeather = self.WeatherObject.GetCurrentWeather()
		self.CurrentTemperature = self.WeatherObject.GetCurrentTemperature()
		return [self.CurrentWeather,self.CurrentTemperature]

	def GetCityNames(self):
		'''
			Returns the city names in a list.

			Useful if you have multiple city names in a string
			and you want to use anyone of the names.

			example:
				>> Whats the weather in London and New York and San Jose and San Francisco

				.. ['London', 'New York', 'San Jose', 'San Francisco']


		'''
		return self.CityName



class ShowWeatherConditions(object):

	
	def __init__(self,data,place):
		# The data argument can be any list.
		self.data = data
		self.place = place

	def FormatWeatherConditions(self):
		# user friendly responses
		self.WeatherResp = ["It's {2}C and {0} in {1}"]
		return self.WeatherResp[0].format(self.data[0],self.place,self.data[1])

if __name__== '__main__':

	w = WexWeather("whats the weather in London","[API-KEY]")
	print(w.WexGetWeather())