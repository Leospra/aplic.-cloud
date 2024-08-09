import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Função para treinar e salvar o modelo
def train_model():
    # Simulação de dados de treino
    data = {
        'motor_temp': [70, 75, 80, 85, 90],
        'generator_temp': [65, 70, 75, 80, 85],
        'fridge_temp': [5, 6, 7, 8, 9],
        'target': [72, 76, 81, 86, 91]
    }
    df = pd.DataFrame(data)
    X = df[['motor_temp', 'generator_temp', 'fridge_temp']]
    y = df['target']

    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, 'model.pkl')

# Função para carregar o modelo
def load_model():
    return joblib.load('model.pkl')

# Função para prever a temperatura
def predict_temperature(model, features):
    return model.predict(features)
