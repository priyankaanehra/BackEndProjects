
## WeatherAPI ☀️🌧️
A lightweight Flask API that fetches weather data for a given city using the Visual Crossing Weather API. Includes caching with Redis and basic rate-limiting.

### 🔧 Features
- 🔍 Search weather by city
- ⚡ Caching with Redis (12-hour expiration)
- 🛡️ Rate-limited to 10 requests per minute per IP
- 🌐 Uses the [Visual Crossing Weather API](https://www.visualcrossing.com/weather-data-editions)

### 🏁 Getting Started
### 1. Set up virtual environment: 
python3 -m venv venv
source venv/bin/activate
### 2. Install dependencies: 
pip install -r requirements.txt
### 3. Create .env file
### 5. Run the server
python app.py

### API USAGE:

Browser: http://127.0.0.1:5000/weather?city=Toronto
```json
{
  "source": "api",
  "data": {
    ...
  }
}
```
If cached, "source": "cache" will be shown instead.