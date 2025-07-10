import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
import api_call
import times
from typing import cast
import time
from datetime import datetime
import sys
import logging
from logging.handlers import RotatingFileHandler

# Configure logging
def setup_logging():
    """Configure logging with both file and console handlers"""
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    # Configure root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # Format for logs
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # File handler (rotating log files)
    file_handler = RotatingFileHandler(
        'logs/weather_service.log',
        maxBytes=1024 * 1024,  # 1MB
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger

# Create logger for this module
logger = logging.getLogger(__name__)

def get_weather_message(temp: float, feels_temp: float) -> str:
    """Generate a weather message based on conditions"""
    if feels_temp >= 95:
        return f"🔥 FURNACE OF DESPAIR: It feels like {feels_temp:.1f}°F (actually {temp:.1f}°F). May God have mercy on your soul."
    elif feels_temp >= 85:
        return f"🌡️ TOO HOT: A steamy {feels_temp:.1f}°F (actually {temp:.1f}°F). Consider moving to Alaska."
    elif feels_temp >= 75:
        return f"😅 WARM: {feels_temp:.1f}°F (actually {temp:.1f}°F). Getting a bit toasty out there."
    elif feels_temp >= 65:
        return f"👌 PERFECT: A pleasant {feels_temp:.1f}°F (actually {temp:.1f}°F). Enjoy it while it lasts!"
    elif feels_temp >= 50:
        return f"🧥 COOL: {feels_temp:.1f}°F (actually {temp:.1f}°F). Grab a light jacket."
    elif feels_temp >= 32:
        return f"❄️ COLD: {feels_temp:.1f}°F (actually {temp:.1f}°F). Winter is coming."
    else:
        return f"🥶 FROZEN WASTELAND: A brutal {feels_temp:.1f}°F (actually {temp:.1f}°F). Why do you live here?"

def send_weather_update():
    """Send a single weather update"""
    try:
        # Get email configuration
        sender = cast(str, os.getenv('EMAIL_SENDER'))
        app_password = cast(str, os.getenv('EMAIL_APP_PASSWORD'))
        recipient = cast(str, os.getenv('EMAIL_RECIPIENT'))
        
        if not all([sender, app_password, recipient]):
            raise ValueError("Missing email configuration")
        
        # Get weather data
        temp = api_call.get_weather_data()
        current_time = times.current_time()
        
        if any(v is None for v in [temp, api_call.feel_temp, api_call.formatted_time]):
            raise ValueError("Failed to get weather data")
            
        # Generate weather message
        weather_message = get_weather_message(temp, api_call.feel_temp)
        
        # Prepare email
        msg = EmailMessage()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = f"Weather Update - {datetime.now().strftime('%I:%M %p')}"
        msg.set_content(
            f"Weather Status\n"
            f"-------------\n"
            f"Time: {current_time}\n"
            f"{weather_message}\n"
            f"Sunset: {api_call.formatted_time}"
        )
        
        # Send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, app_password)
            smtp.send_message(msg)
            
        logger.info(f"Update sent successfully at {current_time}")
        
    except Exception as e:
        logger.error(f"Error sending update: {str(e)}", exc_info=True)
        # Don't exit on error, just log it and continue

def main():
    logger.info("Starting Weather Update Service...")
    load_dotenv()
    
    # How often to check (in seconds)
    UPDATE_INTERVAL = 30 * 60  # 30 minutes
    
    try:
        while True:
            send_weather_update()
            
            # Sleep until next update
            next_update = datetime.now().strftime('%I:%M %p')
            logger.info(f"Next update scheduled for: {next_update}")
            time.sleep(UPDATE_INTERVAL)
            
    except KeyboardInterrupt:
        logger.info("Shutting down weather service...")
        sys.exit(0)

if __name__ == "__main__":
    setup_logging()
    main()