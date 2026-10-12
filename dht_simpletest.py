import time

import board

import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D18)

while True:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(f"Temp: {temperature_c:.1f} C / {temperature_f:.1f} F    Humidity: {humidity}% ")
