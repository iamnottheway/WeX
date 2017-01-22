
# WeX : A python weather extractor :earth_americas::sun_with_face::cloud:

Have you ever wanted to know, the current weather of a place, from a city name in a string? 
I guess you have thought of it some time in your life. :umbrella: :sunny: :snowman:

Well, WeX does that for you :)

WeX reads a string and looks for a city name, then it gives the current weather conditions of the city.


## Documentation will be added :page_facing_up::bell::book::computer::computer:

## Why should you use it?And Where can you use it?

  If you are building a chatbot and you want to make the bot give the current weather of a city by reading
  a string you can use WeX. Or if you want to make an app which responds to your voice and shows you the weather,
  you can use WeX.
  
  And if you want to make a mod for a game which makes the weather change in the game, when it actually changes
  in the real world.

## Installation:electric_plug::electric_plug: 

        * pip install package will be added soon (Learning to create a package :) )
        * Download or clone the repository
        * Put the Extractor folder in any folder you want
        * Done!
       
       Start by import:
       
                from Extractor import Wex

###What does it do?
    
    // This is the input
    >> What is the weather in London?
    
    // This is the output
    .. It's Clouds in London with 1.15C

    
**_How does it work?_**:wrench::nut_and_bolt:
-----------------
```python
from Extractor import Wex
from Extractor.Wex import FormatWeatherConditions
            
weather = Wex.WexWeather("Whats the weather in London?","[API-Key]")
            
data = weather.WexGetWeather()
            
 weather = FormatWeatherConditions(data)
            
print(weather)
```
 
That's it. Just tiny bit of code to get the current weather of London.:memo:

About Contributing  :busts_in_silhouette::speech_balloon::bust_in_silhouette:
--------------------

All Contributions are welcome. If there is any issue or a bug open an issue.

All of your help will be considered. Help make this project reach many people,
so that they can use this in their projects :) 

    
Note :speaker::speaker::speaker:
-----
 * Depends on geotext library to extract places(It's included)  https://github.com/elyase/geotext
   To install geotext library, run that in the terminal.
   Read more about geotext on https://geotext.readthedocs.io/en/latest/ :earth_americas: :palm_tree: :sun_with_face:
   
   ###Installing geotext
   for python2
    ```
     pip install geotext
    ```
          
    for python3
    ```
     pip3 install geotext 
    ```
 
 * weather data from https://openweathermap.org/
   Create an account and use the API key to use this. Supply the API-key when creating the object:zap:
 * The output responses have been changed. 

:doughnut::coffee::beers::evergreen_tree:







