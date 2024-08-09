import paho.mqtt.client as mqtt
import json
import requests

# Configurações do MQTT
MQTT_BROKER = 'broker.hivemq.com'
MQTT_PORT = 1883
MQTT_TOPIC = 'sensor/temperature'

# Função chamada quando uma nova mensagem é recebida
def on_message(client, userdata, message):
    try:
        # Converter a mensagem para JSON
        payload = json.loads(message.payload.decode())
        
        # Enviar dados para o servidor Flask
        response = requests.post('http://localhost:5000/sensor_data', json=payload)
        print(f'Status do servidor: {response.status_code}, Resposta: {response.json()}')
        
    except Exception as e:
        print(f'Erro: {e}')

# Configuração do cliente MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)

# Loop de espera de mensagens
client.loop_forever()
