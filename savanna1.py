import json
import flask
import paho.mqtt.client as mqtt
import time
import socket

app = flask.Flask(__name__)

# Callback functions: log, connect, disconnect, and message received
def on_log(client, userdata, level, buf):
    print("log: " + buf) 

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe("Strathmore/LoRa_gateway")  # Subscribe to the topic after a successful connection
        publish_ip_address(client)
    else:
        print(f"Bad connection. Returned code={rc}. Retrying in 5 seconds...")
        time.sleep(5)
        client.reconnect()

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected. Result code " + str(rc))

def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    print("Message received", m_decode)

def publish_ip_address(client):
    ip_address = get_ip_address()
    client.publish("Strathmore/LoRa_gateway", ip_address)

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

# Broker details
broker = "broker.emqx.io"
Port = 1883 

# New instance of the MQTT client created
client = mqtt.Client("Python1")

# Bind callback functions
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# Endpoint for getting IP address
@app.route('/get_ip_address', methods=['GET'])
def get_ip_address_endpoint():
    ip_address = get_ip_address()
    result = {"output": ip_address}
    return json.dumps(result)

if __name__ == '__main__':
    while True:
        try:
            print("Connecting to broker", broker)
            client.connect(broker)
            client.loop_forever()
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Connection failed: {str(e)}. Retrying in 5 seconds...")
            time.sleep(5)
