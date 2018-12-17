"""
`sig7seg example display`
====================================================
Example usage for sig7seg circuitpython library.
https://github.com/b3nn/Sig7Seg-i2c-mpy
* Author(s): b3nn
"""

# You will need adafruit_bus_device and adafruit_mcp230xx.mpy
# along with sig7seg.mpy in your *lib* directory
import board
import time
import busio
from sig7seg import sig7seg

# Init the i2c bus to pass to sig7seg
i2c = busio.I2C(board.SCL, board.SDA)
sig = sig7seg(i2c)

# Write a number to the display
sig.write(6)
time.sleep(1)

# Count up on the display
for x in range(0, 16):
    sig.write(x)
    time.sleep(.1)

# Clear the display
sig.clear()

def draw_segements(sig, delay):
    sig.clear()
    segments = 1
    for i in range (0, 8):
        sig.set_segements(segments)
        segments = (segments << 1) + 1
        time.sleep(delay)

# Flip on each segment one at a time with 100ms delay
draw_segements(sig, 0.1)


