"""
Example usage of WeatherApp
Demonstrates different ways to use the weather application
"""

from weather_app import WeatherApp

def example_single_city():
    """Example: Query weather for a single city"""
    print("=" * 50)
    print("Example 1: Single City Query")
    print("=" * 50)
    
    app = WeatherApp(api_key="your_api_key_here")
    
    # Query weather for Beijing
    weather_data = app.get_weather("Beijing")
    
    if weather_data:
        print(app.format_weather_info("Beijing", weather_data))
    else:
        print("Failed to get weather data")

def example_multiple_cities():
    """Example: Query weather for multiple cities"""
    print("=" * 50)
    print("Example 2: Multiple Cities Query")
    print("=" * 50)
    
    app = WeatherApp(api_key="your_api_key_here")
    
    cities = ["Beijing", "Shanghai", "Guangzhou", "Shenzhen"]
    app.display_multiple_cities(cities)
    
    # Save the data
    app.save_to_file("weather_data.json")

def example_fahrenheit():
    """Example: Query weather in Fahrenheit"""
    print("=" * 50)
    print("Example 3: Weather in Fahrenheit")
    print("=" * 50)
    
    app = WeatherApp(api_key="your_api_key_here")
    
    # Query weather in Fahrenheit
    weather_data = app.get_weather("New York", units="imperial")
    
    if weather_data:
        print(app.format_weather_info("New York", weather_data))
    else:
        print("Failed to get weather data")

def example_error_handling():
    """Example: Error handling"""
    print("=" * 50)
    print("Example 4: Error Handling")
    print("=" * 50)
    
    app = WeatherApp(api_key="your_api_key_here")
    
    # Try to query a non-existent city
    print("\nQuerying non-existent city...")
    weather_data = app.get_weather("InvalidCityXYZ")
    
    if weather_data is None:
        print("❌ Failed to get weather (expected behavior)")
    
    # Try to query with invalid API key
    print("\nQuerying with invalid API key...")
    app_invalid = WeatherApp(api_key="invalid_key")
    weather_data = app_invalid.get_weather("Beijing")
    
    if weather_data is None:
        print("❌ Failed to get weather (expected behavior)")

def example_programmatic_access():
    """Example: Programmatic access without interactive mode"""
    print("=" * 50)
    print("Example 5: Programmatic Access")
    print("=" * 50)
    
    app = WeatherApp(api_key="your_api_key_here")
    
    # Get weather data
    weather_data = app.get_weather("Tokyo")
    
    if weather_data:
        # Access specific weather information
        main_data = weather_data.get("main", {})
        wind_data = weather_data.get("wind", {})
        
        temp = main_data.get("temp")
        humidity = main_data.get("humidity")
        wind_speed = wind_data.get("speed")
        
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        
        # You can process this data however you want
        if temp > 25:
            print("🌞 It's hot outside!")
        elif temp < 10:
            print("❄️ It's cold outside!")
        else:
            print("🌤️ The weather is moderate")

if __name__ == "__main__":
    print("\n🌍 WeatherApp - Usage Examples\n")
    
    # Uncomment the example you want to run:
    
    # example_single_city()
    # example_multiple_cities()
    # example_fahrenheit()
    # example_error_handling()
    # example_programmatic_access()
    
    print("\n" + "=" * 50)
    print("To run these examples:")
    print("1. Replace 'your_api_key_here' with your actual API key")
    print("2. Uncomment the function call you want to run")
    print("3. Run this script: python example_usage.py")
    print("=" * 50)