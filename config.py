"""
Configuration file for WeatherApp
Store your API key and other settings here
"""

# OpenWeatherMap API Key
# Get your free API key at: https://openweathermap.org/api
OPENWEATHER_API_KEY = "your_api_key_here"

# Temperature unit: "metric" for Celsius, "imperial" for Fahrenheit
TEMPERATURE_UNIT = "metric"

# Default output file for saving weather data
DEFAULT_OUTPUT_FILE = "weather_data.json"

# API endpoint
API_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Request timeout in seconds
REQUEST_TIMEOUT = 5

# List of favorite cities (optional)
FAVORITE_CITIES = [
    "Beijing",
    "Shanghai",
    "Guangzhou",
    "Shenzhen"
]