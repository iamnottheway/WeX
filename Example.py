
# This program gets londons weather

#import the Wex module
from Extractor import Wex
# Import the FormatWeatherConditions() function from the Wex module
from Extractor.Wex import FormatWeatherConditions

# create a weather object
weather = Wex.WexWeather("Whats the weather in London?","396cbf110cc7bd1bd3087f317643a83f")
# call the WexGetWeather() method to get the weather data
# Then you can directly print the data
# It will output a list containing the data
data = weather.WexGetWeather()
# But let's make it friendly by using the FormatWeatherConditions(arg)
# takes a list as an argument
weather = FormatWeatherConditions(data)
print(weather)