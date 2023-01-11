import RPi.GPIO as GPIO

# Constants
# GPIO
# Relay signal pin
PIN_IMP = 7

# GPIO Initialization
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # Set GPIO mode to BOARD
GPIO.setup(PIN_IMP, GPIO.OUT) # Sets relay as output

# Relay OFF
GPIO.output(PIN_IMP, GPIO.LOW)

# GPIO Free PINS
GPIO.cleanup()
