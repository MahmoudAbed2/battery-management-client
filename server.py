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
@app.route('/charge', methods=['POST'])
def start_charging():
    global battery_level
    try:
        target = request.json.get('target')
        if battery_level < target:
            while battery_level < target:
                battery_level += 1  # Charge by 1% at a time
        return jsonify({
            "status": "Charging in progress",
            "battery_level": battery_level
        })
    except Exception as e:
        return jsonify({
            "error": f"Error starting charge: {str(e)}"
        }), 500

# Stop charging
@app.route('/stop_charge', methods=['POST'])
def stop_charging():
    global battery_level
    battery_level = 20  # Reset to start level when stopping
    return jsonify({
        "status": "Charging stopped",
        "battery_level": battery_level
    })

# Get current battery level
@app.route('/get_battery_level', methods=['GET'])
def get_battery_level():
    global battery_level
    return jsonify({
        "battery_level": battery_level
    })


@app.route('/baseload', methods=['GET'])
def get_baseload():
    try:
        # Simulerad hushållsförbrukning per timme (24 timmar)
        consumption_data = [random.uniform(0.5, 2.5) for _ in range(24)]  # Exempel på hushållens förbrukning
        avg_consumption = sum(consumption_data) / len(consumption_data)
        return jsonify({
            "baseload": avg_consumption,
            "message": "Genomsnittlig baslast för hushåll"
        })
    except Exception as e:
        return jsonify({
            "error": f"Fel vid hämtning av baslast: {str(e)}"
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
