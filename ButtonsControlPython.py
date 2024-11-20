import serial

# Change for your com port, e.g.: "COM8:", "/dev/ttyUSB0", etc.
serial_port = serial.Serial( port='COM5', baudrate=9600 )  # defaults to N81

while ( True ):
    command = serial_port.read( 2 )  # read 2 bytes from the Arduino
    if ( len( command ) == 2 ):
        if ( command == b'RS' ):
            print( "Arduino was Reset" )
        elif ( command == b'B1' ):
            print( 'received button 01' )
        elif ( command == b'B2' ):
            print( 'received button 02' )
        elif ( command == b'qq' ):
            # Arduino says to quit
            print( 'received QUIT' )
            break

serial_port.close()