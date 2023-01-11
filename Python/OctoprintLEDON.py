import RPi.GPIO as GPIO

# Constants
# GPIO
# Relay signal pin
PIN_IMP = 7

# GPIO Initialization
GPIO.setmode(GPIO.BOARD) # Set GPIO mode to BOARD
GPIO.setup(PIN_IMP, GPIO.OUT) # Sets relay as output

# Relay on
GPIO.output(PIN_IMP, GPIO.HIGH)
