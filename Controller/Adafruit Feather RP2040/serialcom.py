import usb_cdc


class SerialCom:

    def __init__(self):
        self.serial = usb_cdc.data
        self.serial.reset_input_buffer()
        self.serial.reset_output_buffer()


    def SendString(self, string):
        self.serial.write(bytearray(string.encode('utf-8')))


    def GetByte(self):
        while True:
            if self.serial.in_waiting > 0:
                byte = self.serial.read(1)
                self.serial.write(byte)
                return byte


