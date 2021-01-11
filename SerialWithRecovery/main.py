import serial

def initSerial():
    while (1):
        try:
            serialPort = serial.Serial(port="COM3", baudrate=115200, bytesize=8, timeout=1,
                                       stopbits=serial.STOPBITS_ONE, xonxoff=True, parity=serial.PARITY_NONE)
            return serialPort
        except:
            continue


recCnt = 0
serialPort = initSerial()
print("init")
while(1):
    try:
        if (serialPort.is_open):
            textToSend = str(recCnt)
            serialPort.write(textToSend.encode())
            while(1):
                if(serialPort.inWaiting() > 0):
                    serialString = serialPort.readline()
                    print(serialString.decode())
                    recCnt+=1
                    print(recCnt)
                    break
    except:
        serialPort = initSerial()
