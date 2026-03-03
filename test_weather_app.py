"""
Unit tests for WeatherApp
Test weather query functionality
"""

import unittest
from unittest.mock import patch, MagicMock
from weather_app import WeatherApp


class TestWeatherApp(unittest.TestCase):
    """Test cases for WeatherApp"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.app = WeatherApp("test_api_key")
    
    @patch('weather_app.requests.get')
    def test_get_weather_success(self, mock_get):
        """Test successful weather query"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "main": {
                "temp": 25,
                "feels_like": 24,
                "humidity": 65,
                "pressure": 1013,
                "temp_min": 20,
                "temp_max": 30
            },
            "weather": [{"description": "clear sky"}],
            "wind": {"speed": 5, "deg": 180},
            "sys": {"sunrise": 1609459200, "sunset": 1609492800},
            "clouds": {"all": 10}
        }
        mock_get.return_value = mock_response
        
        result = self.app.get_weather("Beijing")
        
        self.assertIsNotNone(result)
        self.assertEqual(result["main"]["temp"], 25)
        self.assertEqual(result["main"]["humidity"], 65)
    
    @patch('weather_app.requests.get')
    def test_get_weather_city_not_found(self, mock_get):
        """Test city not found error"""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        result = self.app.get_weather("NonExistentCity")
        
        self.assertIsNone(result)
    
    @patch('weather_app.requests.get')
    def test_get_weather_invalid_api_key(self, mock_get):
        """Test invalid API key error"""
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_get.return_value = mock_response
        
        result = self.app.get_weather("Beijing")
        
        self.assertIsNone(result)
    
    @patch('weather_app.requests.get')
    def test_get_weather_timeout(self, mock_get):
        """Test timeout error"""
        import requests
        mock_get.side_effect = requests.exceptions.Timeout()
        
        result = self.app.get_weather("Beijing")
        
        self.assertIsNone(result)
    
    def test_format_weather_info(self):
        """Test weather info formatting"""
        test_data = {
            "main": {
                "temp": 25,
                "feels_like": 24,
                "humidity": 65,
                "pressure": 1013,
                "temp_min": 20,
                "temp_max": 30
            },
            "weather": [{"description": "clear sky"}],
            "wind": {"speed": 5, "deg": 180},
            "sys": {"sunrise": 1609459200, "sunset": 1609492800},
            "clouds": {"all": 10}
        }
        
        result = self.app.format_weather_info("Beijing", test_data)
        
        self.assertIn("Beijing", result)
        self.assertIn("25", result)
        self.assertIn("65", result)
        self.assertIn("5", result)
    
    @patch('weather_app.requests.get')
    def test_get_multiple_cities(self, mock_get):
        """Test multiple cities query"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "main": {"temp": 25, "humidity": 65},
            "weather": [{"description": "clear sky"}],
            "wind": {"speed": 5, "deg": 180},
            "sys": {"sunrise": 1609459200, "sunset": 1609492800},
            "clouds": {"all": 10}
        }
        mock_get.return_value = mock_response
        
        cities = ["Beijing", "Shanghai", "Guangzhou"]
        results = self.app.get_multiple_cities(cities)
        
        self.assertEqual(len([r for r in results.values() if r is not None]), 3)


if __name__ == '__main__':
    unittest.main()