
from  w1thermsensor import W1ThermSensor, Unit
from gpiozero import MCP3008
from time import sleep
import adafruit_dht
import board
sensor = W1ThermSensor()
temperature_in_celsius = sensor.get_temperature()
dhtDevice = adafruit_dht.DHT11(board.D18)
f = open("temperatuurwaardes.csv", "w")
volgnummer = 1

while True:
    graden_celsius_DHT11 = dhtDevice.temperature
    potwaarde = MCP3008(channel=0)
    spanning = potwaarde.value * (5 / 1)
    graden_celsius_MCP = (spanning - 0.5) * 100.0
    verschil_temp =  graden_celsius_MCP - graden_celsius_DHT11
    gemiddelde_temp =  (graden_celsius_MCP + graden_celsius_DHT11) / 2

    print(f"{volgnummer}, {graden_celsius_DHT11} --> DHT11, {graden_celsius_MCP} --> MCP3008, {verschil_temp} --> Verschil van DHT11 & MCP3008, {gemiddelde_temp} --> Gemiddelde van DHT11 & MCP3008")
    volgnummer = volgnummer + 1
    
    sleep(3)
    f = open("temperatuurwaardes.csv", "a")
    f.write("\n")
    f.write(f"{volgnummer}, {graden_celsius_DHT11}, {graden_celsius_MCP}, {verschil_temp}, {gemiddelde_temp}")
    f.close()
    









   