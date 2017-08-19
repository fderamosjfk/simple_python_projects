
import requests

def get_weather_forecast():
    url = "http://api.openweathermap.org/data/2.5/weather?q=Orlando,fl&units=imperial&appid=95c18ee308896329007517bdf9787da2"
    weather_request = requests.get(url)
    weather_json = weather_request.json()
    
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    forecast = "The Circus forecast for today is "
    forecast += description + " with a high of " + str(temp_max)
    forecast += " and a low of " + str(temp_min)
    return forecast
