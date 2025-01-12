from flask import Flask, jsonify, request, send_from_directory
import random
from datetime import datetime
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static')  # Serve static files from 'static' folder
CORS(app)  # Enable CORS for all routes

# Serve the HTML file at the root URL
@app.route('/')
def serve_html():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')

# Simulated electricity price per hour for area 3 Stockholm
@app.route('/priceperhour', methods=['GET'])
def get_electricity_price():
    try:
        electricity_price = [random.uniform(0.5, 1.0) for _ in range(24)]
        return jsonify({
            "price_per_hour": electricity_price,
            "area": "Elområde 3 Stockholm"
        })
    except Exception as e:
        return jsonify({
            "error": f"Error fetching electricity price: {str(e)}"
        }), 500  # Server error

# Simulated household consumption per hour
@app.route('/household_consumption', methods=['GET'])
def get_household_consumption():
    try:
        consumption = [random.uniform(0.5, 2.5) for _ in range(24)]
        return jsonify({
            "household_consumption": consumption
        })
    except Exception as e:
        return jsonify({
            "error": f"Error fetching household consumption: {str(e)}"
        }), 500  # Server error

# Simulated battery charging
battery_level = 20  # Start battery level
charging_start_time = None  # Start time of charging
lowest_price_time = None  # Time of lowest price

@app.route('/charge', methods=['POST'])
def start_charging():
    global battery_level, charging_start_time, lowest_price_time
    try:
        target = request.json.get('target')

        # Hämta elpriser för att kolla vilket som är det lägsta priset
        price_data = [random.uniform(0.5, 1.0) for _ in range(24)]
        lowest_price = min(price_data)
        lowest_price_time = price_data.index(lowest_price)

        # Starta laddning om batterinivån är lägre än målet
        if battery_level < target:
            charging_start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Logga starttiden
            while battery_level < target:
                battery_level += 1  # Ladda med 1% åt gången
        return jsonify({
            "status": "Charging in progress",
            "battery_level": battery_level,
            "charging_start_time": charging_start_time,
            "lowest_price_time": lowest_price_time,  # Tidpunkt för lägsta elpris
            "lowest_price": lowest_price  # Det lägsta priset per timme
        })
    except Exception as e:
        return jsonify({
            "error": f"Error starting charge: {str(e)}"
        }), 500
    
    
# Get current battery level
@app.route('/get_battery_level', methods=['GET'])
def get_battery_level():
    global battery_level
    return jsonify({
        "battery_level": battery_level
    })



if __name__ == "__main__":
    app.run(debug=True)
