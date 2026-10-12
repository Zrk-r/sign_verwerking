from gpiozero import LED, MCP3008
from  w1thermsensor import W1ThermSensor

from time import sleep
import board
import adafruit_dht
sensor = W1ThermSensor()
temperature_in_celsius = sensor.get_temperature()
dhtDevice = adafruit_dht.DHT11(board.D18)