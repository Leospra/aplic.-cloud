from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from model import load_model, predict_temperature

app = Flask(__name__)

# Carregar o modelo preditivo
model = load_model()

@app.route('/sensor_data', methods=['POST'])
def receive_sensor_data():
    try:
        data = request.get_json()
        df = pd.DataFrame(data)
        
        # Processar dados e prever a temperatura
        features = df[['motor_temp', 'generator_temp', 'fridge_temp']]
        predictions = predict_temperature(model, features)
        
        response = {
            'status': 'success',
            'predictions': predictions.tolist()
        }
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
