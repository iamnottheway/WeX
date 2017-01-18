"""


Description: Heizenberg is an Intelligent chat bot which can give the
			 User current weather details from around the world.
			 It can also carry simple conversations and suggest users,
			 the wardrob they should wear when going out.


"""

# importing lib's

import re
import random

from geotext.geotext import GeoText



#***************************@ TEXT PROCESSING UNIT @****************************************

class text_processing(object):


	"""

	This class has methods to process the text.
	Methods like uppercase, lowercase, tokenize and sentence parser

	"""

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



class Systematic_txt_checker(object):
	'''docstring for Systematic_txt_checker or STC for short

		The methods of this class use regex to find specific words
		and return true if they exit.

		This method can be used to find what the user is asking.
		And also provide some relevent responces to the user's query.

		Class Methods :
				match_words : searches the string to find words like weather or temperature
								and return the value. This method has one optional argument.
								The optional arg acts as a switch, for the return values

				relevent_word: returns the word list from the match_words() method

	'''
	def __init__(self,string):
		self.string = string


	def match_words(self,*l_switch):
		"""

		Checks the string if words like weather, temperature exists, returns them

		l_switch : Limits the return value for this function
					If there are more than 1 return value, you can set this function to
					return only one. l_switch if it's set to one, then the limit is set to one.
					Only one return value.

		"""

		# for the optional argument : Don't remove this or edit this!
		l_switch_value = None
		for ls in l_switch:
			l_switch_value = ls


		# regular exxpression to find or match with the string
		matched_words = r"[A-Za-z]eath[a-z]*r | [Tt][Ee][A-Za-z]*p[a-z]*"
		# searches for the matched_words in the string
		_final_words = re.findall(matched_words,self.string)


		if l_switch_value == 1:
			if len(_final_words) > 1:
				_final_words = _final_words[0]

		return _final_words

	def relevent_word(self):

		"""
		This method returns the words from the match_words() method.

		This is a return function. Just does it's job!

		"""

		self.rel_word = self.match_words(1)
		return self.rel_word




class Show_details(object):

	"""

	This class is used by the Understand_user() class.
	The Understand_user() class shows the data in a human readable form.
	But, not so formal. Displays It like a bot.

	"""

	def __init__(self,data,place):
		# The data argument can be any list.
		self.data = data
		self.place = place

	def show_Weather_data(self):
		# friendly responses
		self.weather_responses = ["It's {0} in {1} @ {2}C",
									"{0} in {1} with {2}C",
									"Hey, there Here's the weather you wanted\nWeather:{0}\nPlace:{1}\ntemperature:{2}C",
									"It's {2}C and {0} in {1}"
								]
		# chooses a random integer
		random_choice = random.randint(0,len(self.weather_responses))
		# returns the response
		# -------------Test test displaying--------------

		#print(self.weather_responses[3].format(self.data[0],self.place,round(self.data[5],2)))
		#----------------------------------------------------------------------------------------------

		return self.weather_responses[random_choice-1].format(self.data[0],self.place,round(self.data[5],2))



#------------------------------@ Extraction  @----------------------------------------------------


# import the weather_request module which calls the weather JSON data

import weather_request

class ExtractPlaceNames(object):

	def __init__(self,string):
		self.string = string
		# create a Systematic_txt_checker object
		self.Txt_checker = Systematic_txt_checker(self.string)
		# uses GeoText() module to identify the place
		self.city_name = GeoText(self.string).cities
		print(self.city_name)
		# create a weather_request object
		self.weather_obj = weather_request.GetWeatherInfo(self.city_name)


	def Show_Extracted_info(self):
		# call the method to get the relevent word.
		# Here relevent word means, the word which is used as a clue, to find what the user wants to know - like weather
		self.word_list = self.Txt_checker.relevent_word() # returned value is a list

		for x_word in self.word_list:
			# don't know why the comparing doesn't work with string or other list.
			# This just works with the word_list
			if x_word == self.word_list[0]:
				# returns the weather of a certain place
				# Read the weather_request.py documentation for information on usage
				# returns weather, description, pressure and humidity, wind respectivly as a list
				self.weather_data = self.weather_obj.Get_weather()

				# returns the temperature of a place
				self.temperature_data = self.weather_obj.Get_temperature()

				# add temperature_data to the weather_data[0] list
				self.weather_data.append(self.temperature_data[0]) # this is the 5th element
				# create a show_details object to display the weather data
				# now weather_data has 5 elements weather, description, pressure and humidity, wind respectivly as a list

				self.Show_weather_Details = Show_details(self.weather_data,self.city_name[0])
				# access's the show_Weather_data() method to display the data in a nice way;)

				self.friendly_weather_resp = self.Show_weather_Details.show_Weather_data()
				print(self.friendly_weather_resp) # Displays it!






#******************************@ TEST AREA @***********************************************************
# city names must be capitalized
if __name__== '__main__':
	S = ExtractPlaceNames("Whats the weather in New York")
	S.Show_Extracted_info()
