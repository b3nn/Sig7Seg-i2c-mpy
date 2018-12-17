# Sig7Seg-i2c-mpy
A CircuitPython library for the sig7seg-i2c controller 

This library allows you to easily set numbers or segments on displays connected with the sig7seg-i2c controller using CircuitPython.

# Work in Progress!!!
This is still beta code and has not been fully tested yet. Currently using a Trinket M0.

## Install
Copy the `sig7seg.mpy` file to the `lib` directory on the microcontroller.

This also requires two additional libraries from Adafruit in order to run. 
 * [Bus Device](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/releases)
 * [Adafruit MCP230xx library](https://github.com/adafruit/Adafruit_CircuitPython_MCP230xx/releases)

Download the release builds of both of these. Extract the MCP230xx files and copy the `adafruit_mcp230xx.mpy` file to your `lib` directory on the microcontroller. For the Bus Device, extract the `adafruit_bus_device` directory and copy it to the `lib` directory (you do not need `spi_device.mpy` if you want to save space).

## Usage

Make sure to include both the library and `busio`
```
import busio
from sig7seg import sig7seg
```

Now you are ready to create a new sig7seg object
```
i2c = busio.I2C(board.SCL, board.SDA)
sig = sig7seg(i2c)
# Display the number 8
sig.write(8)
```
See the [examples](examples) folder for more details.

## Addresses 

Up to 8 boards can be chained together on the same i2c bus. The mcp23017 has a default address of 0x20. The Sig7Seg library allows an offset from there to be passed in when initializing.

```
sig1 = sig7seg(i2c, 0x01)
sig2 = sig7seg(i2c, 0x02)
sig3 = sig7seg(i2c, 0x03)
```
The address pins must have a jumper to pull the address either high or low. The board will not work correctly without these jumpers. The following table maps the pins to the proper address value

| A0 | A1 | A2 | Begin Hex |
|----|----|----|-----------|
|  0 |  0 |  0 |  0x00     |
|  1 |  0 |  0 |  0x01     |
|  0 |  1 |  0 |  0x02     |
|  1 |  1 |  0 |  0x03     |
|  0 |  0 |  1 |  0x04     |
|  1 |  0 |  1 |  0x05     |
|  0 |  1 |  1 |  0x06     |
|  1 |  1 |  1 |  0x07     |

CircuitPython will throw an error `ValueError: No I2C device at address:` if it is not able to find a controller at the given address.

## LICENSE
Copyright 2018 b3nn

Licensed under the MIT license
