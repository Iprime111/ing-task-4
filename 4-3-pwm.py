import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(24, gpio.OUT)

pwm = gpio.PWM(24, 1000)
pwm.start(0)

try:
    while True:
        d = float(input("Enter duty cycle: "))
        pwm.start(d)
        print(f"Assumed voltage: {d / 100 * 3.3}V")

finally:
    pwm.stop()
    gpio.cleanup()