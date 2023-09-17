import serialcom
import board
import digitalio


class Shell:

    def __init__(self, comCh):
        self.comCh = comCh
        self.commands = {
            'relays',
            'relay',
            'version',
            'help'
        }
        self.current_command = dict()
        self.relay1control = digitalio.DigitalInOut(board.SDA)
        self.relay1control.direction = digitalio.Direction.OUTPUT
        self.relay1control.value = False

        self.relay2control = digitalio.DigitalInOut(board.SCL)
        self.relay2control.direction = digitalio.Direction.OUTPUT
        self.relay2control.value = False


    def Welcome(self):
        self.comCh.SendString(f"\n\n\n")
        self.comCh.SendString(f"=====================================================\n")
        self.comCh.SendString(f"RelayControl v1.0.0\n")
        self.comCh.SendString(f"  https://github.com/hikerguy1900/SerialRelayControl\n")
        self.comCh.SendString(f"  Enter, help, to access documentation.\n")
        self.comCh.SendString(f"=====================================================\n")
        self.comCh.SendString(f"\n")
        self.comCh.SendString("> ")

    def CommandProcessor(self, string):
        self.CommandParse(string)
        self.RunCommand()
        self.comCh.SendString("> ")


    def CommandParse(self, string):
        self.current_command = dict()
        self.current_command['args'] = []
        cmd_parts = string.split()
        num_parts = len(cmd_parts)
        if num_parts != 0:
            for index in range(num_parts):
                print(cmd_parts[index])
                if index == 0:
                    self.current_command['cmd'] = cmd_parts[index]
                elif cmd_parts[index][0] == '-':
                    self.current_command[cmd_parts[index][1]] = cmd_parts[index + 1]
                    index = index + 1
                else:
                    self.current_command['args'].append(cmd_parts[index])
        print(self.current_command)


    def RunCommand(self):
        if 'cmd' in self.current_command:
            print(f"current_command: {self.current_command}")
            cmd_str = self.current_command['cmd']
            if cmd_str == 'help':
                self.CommandHelp()
            elif cmd_str == 'version':
                self.CommandVersion()
            elif cmd_str == 'relay':
                self.CommandRelay()
            elif cmd_str == 'relays':
                self.CommandRelays()
            else:
                self.comCh.SendString(f"Unknown command: {cmd_str}. Enter, help, to access documentation.\n")


    def CommandHelp(self):
        print(len(self.current_command))
        if len(self.current_command['args']) == 1:
            if self.current_command['args'][0] == 'relays':
                self.comCh.SendString(f"Relays:\n")
                self.comCh.SendString(f"  -s <on|off>\n")
                self.comCh.SendString(f"  Example: relays -s off\n")
            elif self.current_command['args'][0] == 'relay':
                self.comCh.SendString(f"Relay:\n")
                self.comCh.SendString(f"  -n <1|2>\n")
                self.comCh.SendString(f"  -s<on|off>\n")
                self.comCh.SendString("\n")
                self.comCh.SendString(f"  Example: relay -n 1 -s off\n")
            elif self.current_command['args'][0] == 'version':
                self.comCh.SendString("Outputs version information for this system\n")
            else:
                self.CommandHelpGeneral()
        else:
            self.CommandHelpGeneral()


    def CommandHelpGeneral(self):
        self.comCh.SendString(f"Supported Commands\n")
        self.comCh.SendString(f"  relays : Actions on all relays.\n")
        self.comCh.SendString(f"  relay  : Actions on a single relay.\n")
        self.comCh.SendString(f"  version: Get system version.\n")
        self.comCh.SendString(f"  help   : Get help for a specific command.\n")
        self.comCh.SendString("\n")
        self.comCh.SendString(f"  Example: help relays\n")

    def CommandRelay(self):
        print("Relay")
        if len(self.current_command) != 4:
            self.comCh.SendString(f"Invalid inputs.\n")
            self.comCh.SendString(f"Enter, help relays, to see command options.\n")
            return
        if 's' in self.current_command and 'n' in self.current_command:
            requested_state = self.current_command['s']
            if requested_state != 'on' and requested_state != 'off':
                self.comCh.SendString(f"Relay number ({requested_state}) is not supported.\n")
                self.comCh.SendString(f"Enter, help relay, to see command options.\n")
                return
            relay_num = self.current_command['n']
            if relay_num != '1' and relay_num != '2':
                self.comCh.SendString(f"Relay number ({relay_num}) is not supported.\n")
                self.comCh.SendString(f"Enter, help relay, to see command options.\n")
                return
            if relay_num == '1':
                if requested_state == "on":
                    self.relay1control.value = True
                elif requested_state == "off":
                    self.relay1control.value = False
            if relay_num == '2':
                if requested_state == "on":
                    self.relay2control.value = True
                elif requested_state == "off":
                    self.relay2control.value = False
        else:
            self.CommandInvalidInputs(self.current_command['cmd'])


    def CommandRelays(self):
        if len(self.current_command) != 3:
            self.CommandInvalidInputs(self.current_command['cmd'])
            return
        if 's' in self.current_command:
            requested_state = self.current_command['s']
            if requested_state == 'off':
                print("Relays: off")
                self.relay1control.value = False
                self.relay2control.value = False
            elif requested_state == 'on':
                print("Relays: on")
                self.relay1control.value = True
                self.relay2control.value = True
            else:
                self.comCh.SendString(f"Requested state ({requested_state}) is not supported.\n")
                self.comCh.SendString(f"Enter, help relays, to see command options.\n")
        else:
            self.CommandInvalidInputs(self.current_command['cmd'])

    def CommandInvalidInputs(self, cmd_str):
        self.comCh.SendString(f"Invalid inputs.\n")
        self.comCh.SendString(f"Enter, help {cmd_str}, to see command options.\n")


    def CommandVersion(self):
        self.comCh.SendString(f"RelayControl v1.0.0\n")
        self.comCh.SendString(f"  https://github.com/hikerguy1900/SerialRelayControl\n")


