import requests
import redis
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

load_dotenv()
app = Flask(__name__)

limiter = Limiter(key_func=get_remote_address)
limiter.init_app(app)

redis_url = os.getenv("REDIS_URL")
r = redis.Redis.from_url(redis_url)

# https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/[location]/[date1]/[date2]?key=YOUR_API_KEY
weather_api_key = os.getenv("WEATHER_API_KEY")
weather_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

# Caching expiration time in seconds (12 hours)
CACHE_EXPIRATION = 43200

@app.route('/weather',methods=['Get'])
@limiter.limit("10 per minute")
def get_weather():
    city = request.args.get('city')

    if not city: 
        return jsonify({"error":"City parameter is required"})
    
    cached_weather = r.get(city)
    if cached_weather:
        return jsonify({
            "source":"cache",
            "data":cached_weather.decode('utf-8')
        })
    
    try:
        response = requests.get(f"{weather_url}{city}",
                                 params=
                                 {'key':weather_api_key,'unitGroup':'metric'})
        if response.status_code!=200:
            return jsonify({"error":"Failed to retireve data from API"}), 500
        data = response.json()

        r.setex(city, CACHE_EXPIRATION, str(data))

        return jsonify({
            "source":"api",
            "data":data
        })
    except request.RequestException as e:
        return jsonify({"error":str(e)}),500
    
if __name__=='__main__':
    app.run(debug=True)