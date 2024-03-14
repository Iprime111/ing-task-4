import RPi.GPIO as gpio

dac = [8, 11, 7, 1, 0, 5, 12, 6]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def IsNumber(string):
    try:
        float(string)
        return True
    except:
        return False

def IsInteger(string):
    try:
        int(string)
        return True
    except:
        return False

try:
    while True:
        strInput = input("Enter a single number in range 0...255: ")

        if strInput == 'q':
            break

        if not(IsNumber(strInput)):
            print("String is not a number")
            continue

        if not(IsInteger(strInput)):
            print("String is not an integer")
            continue

        number = int(strInput)

        if number < 0:
            print("Value is below zero")
            continue

        if number > 255:
            print("Value is too big")
            continue

        print(f"Assumed voltage is {round(number / 256 * 3.3, 3)}V")
        gpio.output(dac, dec2bin(number))
finally:
    gpio.output(dac, 0)
    gpio.cleanup()