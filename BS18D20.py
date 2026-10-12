from  w1thermsensor import W1ThermSensor, Unit
sensor = W1ThermSensor()
temperature_in_celsius = sensor.get_temperature()

while True:
    temperature_in_celsius = sensor.get_temperature(Unit.DEGREES_C)
    print(temperature_in_celsius)
    