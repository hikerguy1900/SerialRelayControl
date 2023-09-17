# SerialRelayControl
SerialRelayControl is a hardware and software project that controls two relays via a serial port. The control scheme is a simple shell-like command structure that can be used manually with a program like [Serial (macOS)](https://www.decisivetactics.com/products/serial/) or [PuTTY (Windows)](https://www.chiark.greenend.org.uk/~sgtatham/putty/) or programaticaly in Python, C#, etc.

# Materials
Below are the materials I used. I'm sure others will work with minor modifications to the CircuitPython code.
**Electornics**
* Adafruit Feather RP2040 (PID 4884)
* Valefod Relay Module from Amazon (ASIN B07WQH63FB)
  
**Mechanical**
* M2x8 screws
* 3D printed mounting board (Fusion360)
  
**Software**
* CircuitPython (for Feather RP2040)
* C# (optional example code)

# Serial Commands
Commands are entered in a shell-like interface. The shell prompt is the > character. One can press enter serveral times to see the prompt after connecting their serial software.

The following is a summary of the supported serial commands. Enter, help, in the shell interface for the most up-to-date documentation.

The, relay, command is use to control indiviudaul realys. The -n flag is used to specifyc the relay number (1, 2). the -s flag is used to specify the desired state (on, off). Below is an example.

    > relay -n 1 -s on

The, relays, command is used to change the change of all realys. Becuase all realys are changed only the state flag (-s) is needed.

    > relays -s off

The, version, command will return the currently runing version of the firmare in the Adafruit Feather RP2040.

    > version
    RelayControl v0.0.0
      https://github.com/hikerguy1900/SerialRelayControl
