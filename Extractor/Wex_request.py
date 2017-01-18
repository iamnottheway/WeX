
import sys

class WexExtractor(object):

	'''

	author : freezer9

	This class sends the request to openweather.com to get their weather data.
	This class also acts as a unofficial wrapper to their API

	usage :

		wex = WexExtractor("London","[API-KEY]")
		print(wex.GetJsonData())

	Create an object and suply 2 arguments, the class requiers 2 arguments to get the data.
	
	To get the weather data in json format use the method GetJsonData(), doesn't take any arguments.

	Then print it.

	'''

	defaultURL = "http://api.openweathermap.org/data/2.5/weather?q={0}&APPID={1}"

	def __init__(self,CityName = None,ApiKey = None):

		self.CityName = CityName
		self.ApiKey   = ApiKey

		if self.CityName == None or self.ApiKey == None:
			raise TypeError("Requires arguments! CityName or ApiKey can't be empty")
			sys.exit(1)
		else:
			if len(self.ApiKey) != 32:
				print("Invalid Api Key!")
			else:
				self.SendGetRequest()


	def GetBuiltUrl(self,CityName,ApiKey):
		'''
		returns the url string
		'''
		return self.UrlBuilder(CityName,ApiKey)

	def UrlBuilder(self,CityName,ApiKey):

		'''
		Builds the right url to make a request.
		returns a string
		'''

		if CityName or ApiKey is not empty:
			try:
				self.CityName = CityName
				if len(ApiKey) == 32:
					self.ApiKey   = ApiKey
				else:
					print("Invalid Api key!")
					sys.exit(1)
			except Exception as e:
				print(e)
				sys.exit(1)
		else:
			raise TypeError("Requires arguments! CityName or ApiKey can't be empty")
			sys.exit(1)

		# http://api.openweathermap.org/data/2.5/weather?q=[CITYNAME]&APPID=[APIKEY]
		# base url for the builder
		self.baseURL = "http://api.openweathermap.org/data/2.5/weather"
		self.baseURL += "?q="
		self.baseURL += "{0}&APPID={1}".format(self.CityName,self.ApiKey)
		return self.baseURL

	def SendGetRequest(self):
		try:
			# tries to import requests. If it fails tries again.
			# If it fails again shows error message.
			import requests
		except IOError:
			try:
				import requests
			except IOError as e:
				print(e)

		# gets the url string
		# requests the data using the built url
		try:
			self.WeatherReq = requests.get(self.GetBuiltUrl(self.CityName,self.ApiKey),timeout=10.0)
			if self.WeatherReq.status_code != 200:
				print("Failed to send!")
				try:
					# try to send the request again
					print("Sending again...")
					# if the request fails try sending using the default url, without building the url
					self.WeatherReq = requests.get(defaultURL.format(self.CityName,self.ApiKey),timeout=10.0)
				except requests.exceptions.Timeout:
					print("Server took too long to respond!")
				except requests.exceptions.RequestException as e:
					print("Check if you have an active Internet Connection! Can't send")
        # http exceptions                                                                    
		except requests.exceptions.RequestException as e:
			print("No active internet connection!")
		except requests.exceptions.Timeout:
			print("Server took too long to respond!")

        # try to get the json data
		try:
			self.jsonData = self.WeatherReq.json()
		except TypeError:
			print("Can't get json data!")
		return self.jsonData

	def GetJsonData(self):
		'''

		returns the json data

		'''
		return self.SendGetRequest()

if __name__ == '__main__':
	wex = WexExtractor("London","396cbf110cc7bd1bd3087f317643a83f")
	data = wex.GetJsonData()
	print(data)




