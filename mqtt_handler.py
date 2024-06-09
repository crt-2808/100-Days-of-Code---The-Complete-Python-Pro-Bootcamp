import paho.mqtt.client as mqtt
import time

# Dirección del broker Mosquitto
broker_address = "localhost"

# Lista para almacenar los mensajes del canal hijo
hijo_messages = []

# Función callback cuando el cliente se conecta al broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker")
        client.subscribe("canal/padre")
        client.subscribe("canal/hijo/#")
    else:
        print("Error de conexión, código:", rc)

# Función callback cuando se recibe un mensaje
def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode("utf-8")
    client_id = topic.split("/")[-1]  # Suponiendo que el client_id está en el tópico
    print(f"Mensaje recibido en {topic}: {payload}")

    if topic.startswith("canal/hijo"):
        hijo_messages.append((client_id, payload))
    elif topic == "canal/padre" and payload == "*":
        for client_id, msg in hijo_messages:
            response = f"Mensaje del hijo ({client_id}): {msg}"
            client.publish("canal/padre", response)
            print(f"Publicado en canal/padre: {response}")
    elif topic == "canal/padre":
        print(f"Mensaje en canal padre: {payload}")

# Crear una instancia del cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conectarse al broker
client.connect(broker_address)
client.loop_start()

# Mantener el script en ejecución
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Desconectando del broker...")
    client.loop_stop()
    client.disconnect()
