# SerialRelayControl
SerialRelayControl is a hardware and software project that controls two relays via a serial port. The control scheme is a simple shell-like command structure that can be used manually with a program like [Serial (macOS)](https://www.decisivetactics.com/products/serial/) or [PuTTY (Windows)](https://www.chiark.greenend.org.uk/~sgtatham/putty/) or programmatically in Python, C#, etc.

![screenshot][SRCBoard]
# PC Communication Quick Start
The Adafruit Feather RP2040 exposes two serial (COM) ports over the USB interface with the PC. One of these serial ports is for controlling the relays using the serial commands. The other is the CircuitPython Read Evaluate Print Loop (REPL), which is used for debug. I don't know of a way to predict which serial port will be named what. To determine which PC COM port is for relay control connect your PC serial software to either COM port and then press return a few times. If you see the command prompt (`>`) you are in the relay control port. If you don't see this prompt try the other COM port. On macOS or Linux the serial port will be something like, `/dev/tty.usbmodem<number>`.

Once you have the command prompt (`>`) type `help` to see the latest list of commands. For help on a particular command type `help` followed by the command name. For example, `help relays`.

# Relay Connections
The two relays on the SRC are electrically independent from each other and from the USB control circuitry. A common way to use the relays is to connect your power source to the common terminal and then you are load to the normally open terminal. To send power to the load turn set the relays state to `on`.

![screenshot][BasicSchematic]

# RP2040 Setup

## Install CircuitPython
* Get the latest version of CircuitPython (uf2 file) for the Adafruit Feathre RP2040 board. https://circuitpython.org/board/adafruit_feather_rp2040/
* Press and hold the BOOTSEL button on the end of the RP240, then press the REST button just behind the USB-C connector on the RP2040. Hold both buttons for several seconds. When the LED stops changing color (10 seconds), or a drive named RPI-RP2 shows up, release both buttons. In my experinece on macOS the drive does not show up until after the buttons are released.
* Drag the UF2 file from the previous step into the RPI-RP2 drive. After several seconds the drive should disapear and then a new drive named CIRCUITPY will appear.
* CircuitPython is now installed on the RP2040.

## Install SerialRelayControl
* Drag all of the files from the SerialRelayControl/Controller/Adafruit Feather RP2040/ directory on the the CIRCUITPY.
* Press the RESET button on the RP2040.
* SerialRelayControl should not be running on the RP2040.

# Materials
Below are the materials I used. I'm sure others will work with minor modifications to the CircuitPython code.
**Electronics**
* Adafruit Feather RP2040 (PID 4884)
* Valefod Relay Module from Amazon (ASIN B07WQH63FB)
  
**Mechanical**
* M2x8 screws
* 3D printed mounting board (Fusion360)
  
**Software**
* CircuitPython (for Feather RP2040)
* C# (optional example code)

# Serial Commands
Commands are entered in a shell-like interface. The shell prompt is the `>` character. One can press enter serveral times to see the prompt after connecting their serial software.

The following is a summary of the supported serial commands. Enter, `help`, in the shell interface for the most up-to-date documentation.

The, relay, command is use to control individual relays. The `-n` flag is used to specific the relay number (`1`, `2`). the `-s` flag is used to specify the desired state (`on`, `off`). Below is an example.

    > relay -n 1 -s on

The, relays, command is used to change the change of all relays. Because all relays are changed only the state flag (`-s`) is needed.

    > relays -s off

The, version, command will return the currently running version of the firmware in the Adafruit Feather RP2040.

    > version
    RelayControl v0.0.0
      https://github.com/hikerguy1900/SerialRelayControl


[SRCBoard]: ./Doc/SerialRelayControl.png
[BasicSchematic]: ./Doc/BasicSchematic.png

