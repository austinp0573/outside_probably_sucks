import unittest
from unittest.mock import patch, MagicMock
import os
import sys
import logging
from logging import Logger
from typing import cast
from datetime import datetime

# Add parent directory to path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from weather_service import get_weather_message, send_weather_update, setup_logging

class TestWeatherService(unittest.TestCase):
    """Test cases for weather service functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Disable logging for tests
        logging.disable(logging.CRITICAL)
    
    def tearDown(self):
        """Clean up test fixtures"""
        # Re-enable logging
        logging.disable(logging.NOTSET)
    
    def test_get_weather_message(self):
        """Test weather message generation for different temperatures"""
        test_cases = [
            (100, 98, "🔥 FURNACE OF DESPAIR"),
            (87, 88, "🌡️ TOO HOT"),
            (77, 78, "😅 WARM"),
            (68, 67, "👌 PERFECT"),
            (55, 54, "🧥 COOL"),
            (35, 34, "❄️ COLD"),
            (25, 20, "🥶 FROZEN WASTELAND"),
        ]
        
        for temp, feels_temp, expected_start in test_cases:
            message = get_weather_message(temp, feels_temp)
            self.assertTrue(
                message.startswith(expected_start),
                f"Expected message to start with '{expected_start}' for temp={temp}, feels_temp={feels_temp}"
            )
            self.assertIn(str(temp), message)
            self.assertIn(str(feels_temp), message)
    
    @patch('weather_service.api_call')
    @patch('weather_service.times')
    @patch('smtplib.SMTP_SSL')
    def test_send_weather_update_success(self, mock_smtp, mock_times, mock_api):
        """Test successful weather update sending"""
        # Mock environment variables
        test_env = {
            'EMAIL_SENDER': 'test@example.com',
            'EMAIL_APP_PASSWORD': 'test_password',
            'EMAIL_RECIPIENT': 'recipient@example.com'
        }
        with patch.dict(os.environ, test_env):
            # Mock API responses
            mock_api.get_weather_data.return_value = 75.0
            mock_api.feel_temp = 78.0
            mock_api.formatted_time = "7:30 PM"
            
            # Mock current time
            mock_times.current_time.return_value = "3:00 PM"
            
            # Mock SMTP connection
            mock_smtp_instance = MagicMock()
            mock_smtp.return_value.__enter__.return_value = mock_smtp_instance
            
            # Call function
            send_weather_update()
            
            # Verify SMTP calls
            mock_smtp_instance.login.assert_called_once_with(
                test_env['EMAIL_SENDER'],
                test_env['EMAIL_APP_PASSWORD']
            )
            mock_smtp_instance.send_message.assert_called_once()
    
    @patch('weather_service.api_call')
    def test_send_weather_update_missing_config(self, mock_api):
        """Test weather update with missing configuration"""
        # Mock environment variables (missing some required vars)
        test_env = {'EMAIL_SENDER': 'test@example.com'}
        with patch.dict(os.environ, test_env, clear=True):
            send_weather_update()  # Should log error but not raise exception
            mock_api.get_weather_data.assert_not_called()
    
    def test_setup_logging(self):
        """Test logging setup"""
        logger = cast(Logger, setup_logging())
        
        # Verify logger configuration
        self.assertEqual(logger.level, logging.INFO)
        
        # Verify handlers
        # Note: handlers is a valid attribute of Logger instances, ignore linter error
        handlers = logger.handlers
        self.assertTrue(any(isinstance(h, logging.StreamHandler) for h in handlers))
        self.assertTrue(any(isinstance(h, logging.handlers.RotatingFileHandler) for h in handlers)) # type: ignore
        
        # Clean up test log directory
        log_dir = 'logs'
        if os.path.exists(log_dir):
            for file in os.listdir(log_dir):
                if file.startswith('weather_service'):
                    os.remove(os.path.join(log_dir, file))
            os.rmdir(log_dir)

if __name__ == '__main__':
    unittest.main() 