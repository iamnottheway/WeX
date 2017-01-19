# Needs some fixes So don't use it yet!
# WeX : A python weather extractor 

Have you ever wanted to know, the current weather of a place, from a city name in a string? 
I guess you have thought of it some time in your life. 

Well, WeX does that for you :)

WeX reads a string and looks for a city name, then it gives the current weather conditions of the city.

Here's an example:
    
    // This is the input
    >> What is the weather in New York?
    
    // This is the output
    .. It's Clouds in New York with 1.15C

    
How does it work?
-----------------

    from Extract_Weather import ExtractPlaceNames 

    weather = ExtractPlaceNames("What is the weather in New York")
    weather.Show_Extracted_info()
 
That's it. Just tiny bit of code to get the current weather of New York.

    
Note
-----
 * Depends on geotext library to extract places(It's included)  https://github.com/elyase/geotext
 
 * weather data from https://openweathermap.org/
   Create an account and use the API key to use this.
   Add the API key in weather_requests.py








