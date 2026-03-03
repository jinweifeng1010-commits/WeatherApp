# WeatherApp

A Python weather query application using OpenWeatherMap API

## 📋 Description

WeatherApp is a simple Python application that allows you to query weather information by city name. It supports querying single or multiple cities and displays detailed weather information including temperature, humidity, wind speed, and more.

## ✨ Features

- 🌍 Query weather by city name
- 🏙️ Support for multiple cities in a single query
- 🌡️ Display temperature (current, feels like, min, max)
- 💧 Humidity percentage
- 💨 Wind speed and direction
- ☁️ Cloud coverage percentage
- 🔽 Atmospheric pressure
- 🌅 Sunrise and sunset times
- 📝 Detailed weather descriptions
- 💾 Save weather data to JSON file
- 🎯 Interactive command-line interface

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/jinweifeng1010-commits/WeatherApp.git
cd WeatherApp
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Get a free API key:
   - Visit https://openweathermap.org/api
   - Sign up for a free account
   - Get your free API key from the dashboard

### Usage

Run the application:
```bash
python weather_app.py
```

## 📖 Examples

### Single City Query

```bash
$ python weather_app.py
    Welcome to WeatherApp!

Enter your OpenWeatherMap API key: your_api_key_here

Options:
1. Query single city
2. Query multiple cities
3. Save data to file
4. Exit

Enter your choice (1/2/3/4): 1
Enter city name: Beijing

╔════════════════════════════════════════╗
║     Weather Information for Beijing    ║
╚════════════════════════════════════════╝

🌡️  Temperature:
   Current:     15.5°C
   Feels like:  14.2°C
   Min:         12.0°C
   Max:         18.0°C

💧 Humidity:        65%
🔽 Pressure:        1013 hPa

💨 Wind:
   Speed:       3.5 m/s
   Direction:   180°

☁️  Cloudiness:      20%

📝 Description:     Clear sky

🌅 Sunrise:         08:00:00
🌇 Sunset:          17:12:00
```

### Multiple Cities Query

```bash
Enter your choice (1/2/3/4): 2
Enter city names (separated by comma): Beijing, Shanghai, Guangzhou
```

### Save Data

```bash
Enter your choice (1/2/3/4): 3
Enter filename (default: weather_data.json): my_weather.json
✅ Weather data saved to my_weather.json
```

## 📁 Project Structure

```
WeatherApp/
├── weather_app.py          # Main weather application
├── test_weather_app.py     # Unit tests
├── example_usage.py        # Usage examples
├── requirements.txt        # Project dependencies
├── README.md              # This file
└── .gitignore             # Git configuration
```

## 🧪 Testing

Run the unit tests:

```bash
python -m unittest test_weather_app.py -v
```

Or run tests with more details:

```bash
python -m unittest discover -v
```

## 🔧 Configuration

Create a `config.py` file to store your API key securely (optional):

```python
# config.py
OPENWEATHER_API_KEY = "your_api_key_here"
TEMPERATURE_UNIT = "metric"  # or "imperial"
```

Then modify `weather_app.py` to use the configuration:

```python
from config import OPENWEATHER_API_KEY
app = WeatherApp(api_key=OPENWEATHER_API_KEY)
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add some improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created by: jinweifeng1010-commits

## 🎯 Future Enhancements

- [ ] Add weather forecast functionality (5-day, 10-day, hourly)
- [ ] Support for air quality information
- [ ] Create a graphical user interface (GUI)
- [ ] Add location history/favorites
- [ ] Integration with weather alerts
- [ ] Support for different temperature units
- [ ] Add caching for frequently queried cities
- [ ] Create a web version

## ⚠️ Notes

- The free OpenWeatherMap API has rate limits (1000 calls/day for free tier)
- Some weather data may have slight delays
- City names should be in English
- For more API details, visit: https://openweathermap.org/api

## 📧 Support

If you encounter any issues or have questions, please:
1. Check the existing GitHub Issues
2. Open a new Issue with a detailed description
3. Include error messages and steps to reproduce
