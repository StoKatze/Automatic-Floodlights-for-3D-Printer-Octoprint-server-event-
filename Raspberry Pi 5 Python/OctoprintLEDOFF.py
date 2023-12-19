import gpiod
from gpiod.line import Direction, Value

# Constants
# GPIO
# Chip
CHIP = "/dev/gpiochip4"
# Relay signal pin
PIN_IMP = 4

# Actual program
# Relay on
with gpiod.request_lines(CHIP, consumer="RELAY",
    config={
        PIN_IMP: gpiod.LineSettings(
            # Set as Output
            direction=Direction.OUTPUT, output_value=Value.ACTIVE
        )
    },
) as request:
     request.set_value(PIN_IMP, Value.INACTIVE)

