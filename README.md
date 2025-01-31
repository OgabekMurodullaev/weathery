# Weather App

A Django-based weather forecasting app that provides real-time 
weather updates for various cities around the world.

## Project Purpose

This project aims to fetch and display weather information using the WeatherAPI for multiple cities. 
It helps users to track weather conditions such as temperature, wind speed, and cloud cover.

## Requirements

- Python 3.x
- Django 4.x
- Django REST Framework
- Django Filters
- Requests

Create Virtual Environment
- python -m venv .venv

Activate the virtual environment
- chmod +x ./.venv/bin/activate
- source ./.venv/bin/activate

Install dependencies
- pip install -r requirements.txt

Run migrations to set up the database
- python manage.py migrate

To run and use the project, you will need a SECRET_KEY and a weather API_KEY.
1. Place your secret key in the SECRET_KEY field in the settings.py file.
2. Sign up on https://www.weatherapi.com/ to get an API_KEY and place it in the API_KEY field in the weather app.

To retrieve weather data from the API and save it to the database, you need to run the utils.py 
file within the weather app. This file retrieves weather data from the API and stores it in the 
database.
- python -c "from weather.utils import update_weather; update_weather()"

Start the development server
- python manage.py runserver

Now, to test the API endpoints, we access the URL `api/docs/`.
