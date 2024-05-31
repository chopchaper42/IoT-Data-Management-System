# NSI Homework #5

## Pico MQTT code:

```python
import network
import time
import machine
import ubinascii
from simple import MQTTClient
import urandom

# Wi-Fi Credentials
ssid = 'aaa'
password = '122525625'

# MQTT Configuration
mqtt_broker = 'mqtt.eclipseprojects.io'
mqtt_port = 1883
mqtt_topic = b'pico/temperature'

# Generate a unique client ID based on the MAC address
client_id = ubinascii.hexlify(machine.unique_id())

# Initialize the Wi-Fi connection
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while not wlan.isconnected():
        print('Connecting to WiFi...')
        time.sleep(1)
    
    print('Connected to WiFi:', wlan.ifconfig())

# Publish a random float number to the MQTT broker
def publish_temperature(client):
    while True:
        temperature = urandom.uniform(20.0, 30.0)
        print(f'Publishing temperature: {temperature}')
        client.publish(mqtt_topic, str(temperature))
        time.sleep(20)

# Main function
def main():
    connect_to_wifi()
    
    client = MQTTClient(client_id, mqtt_broker, mqtt_port)
    
    try:
        client.connect()
        print('Connected to MQTT Broker')
        publish_temperature(client)
    finally:
        client.disconnect()
        print('Disconnected from MQTT Broker')

if __name__ == '__main__':
    main()
```


## Pico UART code:

```python
from machine import UART,Pin, Timer
import utime
import random

uart = UART(0, baudrate=9600, tx=0, rx=1)

led = Pin('LED', Pin.OUT)
timer = Timer()
 
def blink(timer):
    led.toggle()
 
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)

while True:
    
    temperature = random.uniform(15.0, 30.0)
    
    uart.write(f'{temperature}\n')
    print(f'{temperature}')
    
    utime.sleep(5)
```