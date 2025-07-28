# Weather Email Notifier

A Python application that automatically sends weather updates via email at regular intervals. It provides personalized weather descriptions based on temperature conditions and includes sunset time information.

## Features

- Real-time weather updates with "feels like" temperature
- Automated email notifications
- Daily sunset time information
- Detailed logging with rotation
- Configurable update intervals
- Fun, personalized weather descriptions
- Continuous operation with error handling

## Setup

1. Clone the repository
2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # Windows
   # OR
   source .venv/bin/activate     # Unix/MacOS
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and fill in your values:
   ```bash
   cp .env.example .env
   ```

5. Edit `.env` with your:
   - OpenWeatherMap API key
   - Gmail sender email and app password
   - Recipient email address

## Usage

Run the weather service:
```bash
python weather_service.py
```

The service will:
1. Start sending periodic weather updates (default: every 30 minutes)
2. Log activities to both console and file
3. Handle errors gracefully and continue running
4. Create rotating log files in the `logs` directory

To stop the service, press Ctrl+C.

## Project Structure

- `weather_service.py`: Main service script that coordinates weather updates
- `api_call.py`: Weather API interaction module
- `times.py`: Time formatting utilities
- `clock.py`: Time display utilities
- `tests/`: Test suite directory
- `logs/`: Log files directory (created automatically)

## Configuration

### Environment Variables
Required variables in `.env`:
- `WEATHER_API_KEY`: Your OpenWeatherMap API key
- `WEATHER_LAT`: Latitude for weather location
- `WEATHER_LON`: Longitude for weather location
- `WEATHER_UNITS`: Temperature units (imperial/metric)
- `EMAIL_SENDER`: Gmail address to send from
- `EMAIL_APP_PASSWORD`: Gmail app password
- `EMAIL_RECIPIENT`: Email address to send to 

### Customization
- Update interval can be modified in `weather_service.py` (UPDATE_INTERVAL)
- Weather message thresholds can be adjusted in the `get_weather_message` function
- Log rotation settings can be configured in the `setup_logging` function

## Testing

Run the test suite:
```bash
python -m unittest discover tests
```

The test suite includes:
- Weather message generation tests
- Email sending functionality tests
- Configuration validation tests
- Logging setup tests

## Logging

The application uses a comprehensive logging system:
- Log files are stored in the `logs` directory
- Files rotate when they reach 1MB
- Keeps up to 5 backup files
- Logs include timestamps, log levels, and full error tracebacks
- Both console and file logging are enabled

## Error Handling

The service is designed to be resilient:
- Catches and logs all exceptions without crashing
- Continues operation after encountering errors
- Validates all required configuration before making API calls
- Includes detailed error messages in logs

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add or update tests as needed
5. Update documentation
6. Submit a pull request

Please ensure your changes:
- Include appropriate tests
- Maintain or improve code coverage
- Follow the existing code style
- Include relevant documentation updates

## License

This project is licensed under the MIT License - see the LICENSE file for details. 

&nbsp;

**466f724a616e6574**