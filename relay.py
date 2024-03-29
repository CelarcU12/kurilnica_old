import RPi.GPIO as GPIO
import time

channel = 21
isOn=False
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)


def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off

def on():
    global isOn
    isOn=True
    GPIO.output(channel, GPIO.LOW)  # Turn motor on
def off():
    global isOn
    isOn=False
    GPIO.output(channel, GPIO.HIGH)  # Turn motor on

def getStatus():
    global isOn
    return isOn

'''
if __name__ == '__main__':
    try:
        motor_on(channel)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
'''