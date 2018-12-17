"""
`sig7seg example 2x display`
====================================================
Example usage for sig7seg-i2c library.
https://github.com/b3nn/Sig7Seg-i2c-mpy
* Author(s): b3nn
"""
import board
import time
import busio
from sig7seg import sig7seg

# Init the i2c bus to pass to sig7seg
i2c = busio.I2C(board.SCL, board.SDA)

sig1 = sig7seg(i2c)
sig2 = sig7seg(i2c, 0x01)

# The 4 inch display can flip faster than the 6 inch ones
# Set the flip time to a 50ms delay
sig1.set_flip_time(0.05)
sig2.set_flip_time(0.05)

# Count up on each display
for x in range(0, 16):
    print(x)
    sig1.write(x)
    sig2.write(x)
    time.sleep(.1)

# Clear all displays
sig1.clear()
sig2.clear()

def draw_segements(sig, delay):
    sig.clear()
    segments = 1
    for i in range (0, 8):
        sig.set_segements(segments)
        segments = (segments << 1) + 1
        time.sleep(delay)

# Flip on each segment one at a time on each 
# display with 100ms delay
draw_segements(sig1, 0.1)
draw_segements(sig2, 0.1)

