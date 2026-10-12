from gpiozero import LED, MCP3008
from time import sleep

led_1 = LED(12)
led_2 = LED(13)
led_3 = LED(14)
led_4 = LED(15)
led_5 = LED(16)
led_6 = LED(17)

while True:
    potwaarde = MCP3008(channel=0)
    voltage = potwaarde.value * (5 / 1)
    degreesC = (voltage - 0.5) * 100.0
    print(f"Voltage: {voltage:.2f} V, Temperature: {degreesC:.2f} °C")

    if degreesC < 5:
        led_1.on()
        led_2.off()
        led_3.off()
        led_4.off()
        led_5.off()
        led_6.off()
    elif 5 <= degreesC < 10:
        led_1.on()
        led_2.on()
        led_3.off()
        led_4.off()
        led_5.off()
        led_6.off()
    elif 10 <= degreesC < 15:
        led_1.on()
        led_2.on()
        led_3.on()
        led_4.off()
        led_5.off()
        led_6.off()
    elif 15 <= degreesC < 20:
        led_1.on()
        led_2.on()
        led_3.on()
        led_4.on()
        led_5.off()
        led_6.off()
    elif 20 <= degreesC < 25:
        led_1.on()
        led_2.on()
        led_3.on()
        led_4.on()
        led_5.on()
        led_6.off()
    else:
        led_1.on()
        led_2.on()
        led_3.on()
        led_4.on()
        led_5.on()
        led_6.on()