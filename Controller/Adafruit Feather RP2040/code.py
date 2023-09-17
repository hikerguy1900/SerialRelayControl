import time
import board
import digitalio
import neopixel
import serialcom
import shell

# Feather RP2040
# Project Pin Assignments
# Relay Board Power: GND, VBUS
# Relay UNC1 Control: GPIO2 (D2)
# Relay UNC2 Control: GPIO3
# Development Mode: GPIO0, GPIO1

# Setup Pins on RP2040

# Class: One Class Per Command <-- Start here?

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.1
pixel.fill((0, 255, 0))

time.sleep(1)

comCh = serialcom.SerialCom()

shell = shell.Shell(comCh)
shell.Welcome()

serialInput = ""
while True:
    byte = comCh.GetByte()
    print(f"Byte Recieved: {byte}")
    pixel.fill((255, 0, 0))
    if byte == b'\x0D': # Carriage Return
        shell.CommandProcessor(serialInput)
        serialInput = ""
    if byte == b'\x0A': # Line Feed
        shell.CommandProcessor(serialInput)
        serialInput = ""
    elif byte == b'\x08': # Backspace
        serialInput = serialInput[:-1]
    else:
        serialInput = f"{serialInput}{byte.decode("utf-8")}"
    pixel.fill((0, 255, 0))

