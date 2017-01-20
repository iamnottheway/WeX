
# WeX : A python weather extractor 

Have you ever wanted to know, the current weather of a place, from a city name in a string? 
I guess you have thought of it some time in your life. 

Well, WeX does that for you :)

WeX reads a string and looks for a city name, then it gives the current weather conditions of the city.

# Documentation will be added

What does it do?
    
    // This is the input
    >> What is the weather in New York?
    
    // This is the output
    .. It's Clouds in London with 1.15C

    
How does it work?
-----------------
            #import the Wex module
            from Extractor import Wex
            from Extractor.Wex import FormatWeatherConditions
            
            weather = Wex.WexWeather("Whats the weather in London?","[API-Key]")
            data = weather.WexGetWeather()
            weather = FormatWeatherConditions(data)
            print(weather)
 
That's it. Just tiny bit of code to get the current weather of London.

About Contributing
--------------------

All Contributions are welcome. If there is any issue or a bug open an issue.
If you know what to do, please to this. 

All of your help will be considered. Help make this project reach many people,
so that they can use this in their projects :)

    
Note
-----
 * Depends on geotext library to extract places(It's included)  https://github.com/elyase/geotext
   To install geotext library, run that in the terminal.
   Read more about geotext on https://geotext.readthedocs.io/en/latest/
            
            pip install geotext
 
 * weather data from https://openweathermap.org/
   Create an account and use the API key to use this.
   Add the API key in weather_requests.py








