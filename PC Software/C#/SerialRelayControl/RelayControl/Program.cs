using System;
using SRC;

using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RelayControl
{
    class Program
    {
        static void Main(string[] args)
        {
            SerialRelayControl m_SerialRelayControl;
            Console.WriteLine("Hello World!");
            m_SerialRelayControl = new SerialRelayControl("COM8");
            m_SerialRelayControl.Connect();
            m_SerialRelayControl.Relay(SerialRelayControl.RelayNum.ONE, SerialRelayControl.RelayState.ON);
            m_SerialRelayControl.Relay(SerialRelayControl.RelayNum.ONE, SerialRelayControl.RelayState.OFF);
            m_SerialRelayControl.Relay(SerialRelayControl.RelayNum.TWO, SerialRelayControl.RelayState.ON);
            m_SerialRelayControl.Relay(SerialRelayControl.RelayNum.TWO, SerialRelayControl.RelayState.OFF);
            m_SerialRelayControl.Disconnect();

        }
    }
}
