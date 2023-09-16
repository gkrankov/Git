# Weather Forecast App

## Overview

This Weather Forecast App is a simple Python application that provides real-time weather information for a specified city. It uses the OpenWeatherMap API to fetch weather data and display it to the user.

## Features

- Current temperature in Celsius.
- Weather description (e.g., sunny, rainy, cloudy).
- Humidity percentage.
- Wind speed in meters per second.

## Prerequisites

Before running the app, ensure you have the following:

- Python 3.x installed.
- An API key from OpenWeatherMap. Get it [here](https://openweathermap.org/api) and replace `YOUR_API_KEY` in the code.

## Installation

Clone or download this repository to your local machine.

Open a terminal or command prompt and navigate to the directory where you've saved the script.

Replace the api_key variable in the script with your own OpenWeatherMap API key. You can obtain a free API key by signing up on the OpenWeatherMap website.

Run the script by entering the following command:
python weather_app.py

You will be prompted to enter the name of a city for which you want to retrieve weather information.

The script will then make an API request to OpenWeatherMap, fetch the weather data for the specified city, and display it in the terminal.

## Script Details

The script consists of two main functions:

get_weather(city_name): This function takes the name of a city as input, makes an API request to OpenWeatherMap, and returns the weather data in JSON format.

display_weather(weather_data): This function takes the weather data as input and prints the relevant information, including the city name, temperature, weather description, humidity, and wind speed.

## Units
By default, the script fetches weather data in metric units (temperature in Celsius, wind speed in meters per second). You can change the units parameter in the params dictionary in the get_weather function to "imperial" if you prefer Fahrenheit and miles per hour.

## License
This script is provided under the MIT License. You can find the license details in the LICENSE file.

## Disclaimer
This script is for educational and personal use only. The accuracy and availability of weather data depend on the OpenWeatherMap API, and usage may be subject to their terms and conditions.
