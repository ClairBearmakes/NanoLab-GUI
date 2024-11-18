from serial.tools.list_ports import comports

for port in comports():
    print(port)

import sys
import glob
import serial


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


if __name__ == '__main__':
    print(serial_ports())

import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))


def ListGCodeFiles_From_FlashDrive(self):
    dir_path = "/media/ron"
    supported_file_type = ".gcode"
    gcode_files_list = []
    
    if len(os.listdir(dir_path)) == 0:
        return gcode_files_list
    
    for path, folders, files in os.walk(dir_path):
        for filename in files:
            file_path = os.path.join(dir_path, filename)
            if supported_file_type in filename:
                gcode_files_list.append(file_path)
                
    return gcode_files_list