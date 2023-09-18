using System;
using System.IO.Ports;

namespace SRC
{
    public class SerialRelayControl 
    {
        public enum RelayNum
        {
            ONE = 0x01,
            TWO = 0x02
        }
        public enum RelayState
        {
            OFF = 0x00,
            ON = 0x01
        }

        private readonly string m_ComPortName;
        private SerialPort m_ComPort;

        public SerialRelayControl(string comPortName)
        {
            m_ComPortName = comPortName;
        }

        public bool Connect()
        {
            if(string.IsNullOrEmpty(m_ComPortName))
            {
                // m_ComPortName must be defined to connect.
                return false;
            }

            if ((m_ComPort != null) && (m_ComPort.IsOpen))
            {
                // Serial port is already open.
                return false;
            }

            m_ComPort = new SerialPort(m_ComPortName);
            m_ComPort.Open();
            if(!m_ComPort.IsOpen)
            {
                // Failed to open port.
                return false;
            }

            // The connection expects a clean start. Empty both the input and
            // output buffers just in case something has been left in them.
            m_ComPort.DiscardInBuffer();
            m_ComPort.DiscardOutBuffer();
            m_ComPort.DtrEnable = true;

            //m_ComPort.DataReceived += ReadCom;
            return true;
        }
        private void ReadCom(object sender, SerialDataReceivedEventArgs e)
        {
            SerialPort sp = (SerialPort)sender;
            int value;
            do
            {
                try { value = sp.ReadByte(); }
                catch (Exception ex)
                {
                    // Abort. Received exception while trying to reset serial port byte.
                    break;
                }
                if (value < 0)
                {
                    // End of stream reached. Read value: {value}. Bytes to read {sp.BytesToRead}.
                    break;
                }
                m_ComPort.Write(value.ToString());
            } while (sp.BytesToRead > 0);
        }

        public void Disconnect()
        {
            m_ComPort.DataReceived -= ReadCom;
            m_ComPort.Close();
        }

        public bool Relay(RelayNum num, RelayState state)
        {
            string cmdStr = $"relay -n {((decimal)num)} -s {state.ToString().ToLower()}\r";
            m_ComPort.WriteLine(cmdStr);
            return true;
        }
    }
}
