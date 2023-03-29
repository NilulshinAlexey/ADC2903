import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)

def dec2bin(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def adc(value):
    GPIO.output(dac, dec2bin(int(value)))


try:
    while True:
        for value in range(256):
            adc(value)
            time.sleep(0.01)
            voltage = 3.3 * value / 256
            compValue = GPIO.input(comp)
            if compValue == 0:
                print("ADC value = {:^3} => input voltage = {:.2f}".format(value, voltage))
                break





finally:
    GPIO.output(dac, 0)