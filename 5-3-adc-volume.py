import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(leds, GPIO.OUT)

def dec2bin(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def adc(value):
    GPIO.output(dac, dec2bin(int(value)))


try:
    while True:
        value, delta = 128, 64
        while delta > 0:
            adc(value)
            time.sleep(0.01)
            voltage = 3.3 * value / 256
            compValue = GPIO.input(comp)
            if compValue == 0:
                value, delta = value-delta, delta//2
            else:
                value, delta = value+delta, delta//2  
        count = (value + 20) // 32
        for i in range(8):
            if i < count:
                GPIO.output(leds[i], 1)
            else: GPIO.output(leds[i], 0)
        print("ADC value = {:^3} => input voltage = {:.2f}".format(value, voltage))





finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)