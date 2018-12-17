"""
`sig7seg`
====================================================

CircuitPython module for the sig7seg_i2c board
https://github.com/b3nn/Sig7Seg-i2c

* Author(s): b3nn
"""
import board
import adafruit_mcp230xx
import digitalio
import time

__version__ = "0.1.0"
__repo__ = "https://github.com/b3nn/Sig7Seg-i2c.git"

class sig7seg:
    
    numbertable = [
      0x3F,  # 0
      0x06,  # 1
      0x5B,  # 2
      0x4F,  # 3
      0x66,  # 4
      0x6D,  # 5
      0x7D,  # 6
      0x07,  # 7
      0x7F,  # 8
      0x6F,  # 9
      0x77,  # A
      0x7C,  # b
      0x39,  # C
      0x5E,  # d
      0x79,  # E
      0x71,  # F
    ]
    
    def __init__(self, i2c, address=0):
        # Match the Arduino code, addresses start at 0x20
        address = address + 0x20
        self.i2c = i2c
        self.mcp = adafruit_mcp230xx.MCP23017(self.i2c, address)
        
        # Sets all the MCP pins to output
        for i in range(0, 16):
            self.mcp.get_pin(i).direction = digitalio.Direction.OUTPUT
        
        self.fliptime = 0.090
        self.i2c.unlock()

    def set_segements(self, bits):
        for i in range(0, 8):
            v = bits & 1
            bits = bits >> 1
            
            # 4-11 are "show" pins on the hardware controller
            pin_show = i
            if i < 4:
                pin_show = i + 8
            
            # If wired correctly, the "hide" pin is always 8 away from the "show" pin
            pin_hide = (pin_show + 8) % 16
            
            # Sets either the "show" or "hide" to high for a segement
            if v:
                self.mcp.get_pin(pin_show).value = True
                self.mcp.get_pin(pin_hide).value = False
            else:
                self.mcp.get_pin(pin_show).value = False
                self.mcp.get_pin(pin_hide).value = True
        
        time.sleep(self.fliptime)
        
        # Power off all pins
        for i in range(0, 16):
            self.mcp.get_pin(i).value = False
        self.i2c.unlock()

    def write(self, num):
        if num > 15:
            return
        if num < 0:
            self.set_dash()
            return
        self.set_segements(self.numbertable[num])
        
    def clear(self):
        self.set_segements(0)
        
    def set_dash(self):
        self.set_segements(0b01000000)
        
    def set_flip_time(self, seconds):
        self.fliptime = seconds