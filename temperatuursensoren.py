from  w1thermsensor import W1ThermSensor, Unit

import time

import board

import adafruit_dht

sensor = W1ThermSensor()
temperature_in_celsius = sensor.get_temperature()

dhtDevice = adafruit_dht.DHT11(board.D18)

while True:

    temperature_verschil =  temperature_in_celsius - temperature_c
    temperature_in_celsius = sensor.get_temperature(Unit.DEGREES_C)

    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
    

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue    
    except RuntimeError as error:
        dhtDevice.exit()
        raise error
    
    time.sleep(2.0)

    if temperature_verschil < 1:
        print("DHT11: ")
        print(f"Temp: {temperature_c:.1f} C / {temperature_f:.1f} F    Humidity: {humidity}% ")
        print("BS18D20:")
        print(temperature_in_celsius)
        print("Led groen is aan")
    elif temperature_verschil > 1 and temperature_verschil < 5:
        print("DHT11: ")
        print(f"Temp: {temperature_c:.1f} C / {temperature_f:.1f} F    Humidity: {humidity}% ")
        print("BS18D20:")
        print(temperature_in_celsius)
        print("Led oranje is aan")
    elif temperature_verschil > 5:
        print("DHT11: ")
        print(f"Temp: {temperature_c:.1f} C / {temperature_f:.1f} F    Humidity: {humidity}% ")
        print("BS18D20:")
        print(temperature_in_celsius)
        print("Led rood is aan")

