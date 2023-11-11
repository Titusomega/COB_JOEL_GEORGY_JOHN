import tkinter as tk
import requests
import datetime as dt
import json
def kelvin_to_celsius_fahrenheit(kelvin):
    celsius=kelvin-273
    fahrenheit=celsius*(9/5)+32
    return celsius,fahrenheit
# Your OpenWeatherMap API Key
API_KEY = 'c4eec169c5029b11ffdd53d58a6c5760'

def fetch_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(base_url)
    data = response.json()
    return data

def display_weather():
    city = city_entry.get()
    weather_data = fetch_weather(city)
    if weather_data["cod"] != "404":
        # Extract relevant weather data from the 
        weather_description = weather_data["weather"][0]["description"]
        temp_kelvin=weather_data['main']['temp']
        temp_celsius,temp_fahrenheit=kelvin_to_celsius_fahrenheit(temp_kelvin)
        feels_like_kelvin=weather_data['main']['feels_like']
        feels_like_celsius,feels_like_fahrenheit=kelvin_to_celsius_fahrenheit(feels_like_kelvin)
        humidity=weather_data['main']['humidity']
        description=weather_data['weather'][0]['description']
        sunrise_time=dt.datetime.utcfromtimestamp(weather_data['sys']['sunrise']+weather_data['timezone'])
        sunset_time=dt.datetime.utcfromtimestamp(weather_data['sys']['sunset']+weather_data['timezone'])
        wind_speed=weather_data['wind']['speed']

        # Update the label with the weather information
        result_label.config(
            text=f"Weather: {weather_description.capitalize()}\nHumidity: {humidity}%\nTemperature in {city}:{temp_celsius:.2f}*C or {temp_fahrenheit:.2f}*F\nTemperature in {city} feels like: {feels_like_celsius:.2f}*C or {feels_like_fahrenheit:.2f}*F\nHumidity in {city}:{humidity}%\nWind Speed in{city}:{wind_speed}m/s\nGeneral Weather in {city}: {description}\nSun rises in {city} at {sunrise_time} local time.\nSun sets in {city} at {sunrise_time} local time."
        )
    else:
        result_label.config(text="City not found")

# Create a basic GUI window
window = tk.Tk()
window.title("Weather App")

# Create and set up widgets
city_label = tk.Label(window, text="Enter City:")
city_entry = tk.Entry(window)
search_button = tk.Button(window, text="Search", command=display_weather)
result_label = tk.Label(window, text="")

# Arrange widgets using grid layout
city_label.grid(row=0, column=0)
city_entry.grid(row=0, column=1)
search_button.grid(row=0, column=2)
result_label.grid(row=1, column=0, columnspan=3)

# Start the GUI application
window.mainloop()
