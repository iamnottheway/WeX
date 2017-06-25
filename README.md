
# Wex : Python weather extractor :earth_americas::sun_with_face::cloud:

Weather Extractor(Wex) is a python library to extract weather data from a string. Wex searches for a city name in a string
and gets you the current weather conditions.

Wex is built for Weather Bots. A Weather Bot can figure out what the text says.Wex is built to make it easier for people to build weatherbots which can get the weather.

##Usage

```python

from Extractor import Wex

weather = Wex.WexWeather("Whats the weather in London?","[API-Key]")

print(weather.WexGetWeather())
            
```

##Output
> ['Clouds', -1.11, 1033.36, 86, 20]


The list contains weather, temperature(c), pressure,humidity,cloud cover


##Requirements
    
 - [GeoText](https://github.com/elyase/geotext) for python2 or python3
  
    Installing GeoText for python2     
     > pip install geotext
          
    for python3
   
     > pip3 install geotext 
   
 - API key from [OpenWeather](https://openweathermap.org/). Create an account and use the API key to use WeX.

(c) 2017 Joel Benjamin


