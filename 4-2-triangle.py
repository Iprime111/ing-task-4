import RPi.GPIO as gpio
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    T = int(input("Enter period: "))
    deltaT = T / 510
    while True:
        for i in range(0, 256):
            gpio.output(dac, dec2bin(i))
            time.sleep(deltaT)

        for i in range(255, -1, -1):
            gpio.output(dac, dec2bin(i))
            time.sleep(deltaT)


finally:
    gpio.output(dac, 0)
    gpio.cleanup()