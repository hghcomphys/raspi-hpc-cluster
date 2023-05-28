import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
while True:
    
    
    read_serial = ser.readline()
    ser.flushOutput()    
    a = int(read_serial, 16)
    print(f'recieved data from arduino: {a:<3d}')
    
    ser.flushOutput()
    write_serial = a
    ser.write(b'%d'%write_serial)

