import serial
import matplotlib.pyplot as plt
from drawnow import *
import atexit
import time

values = []

plt.ion()
cnt = 0

serialArduino = serial.Serial('/dev/cu.usbmodem14201', 9600)


def plotValues():
    plt.ylim(0, 1050)
    plt.xlim(0, 210)
    plt.title('Serial value from Arduino')
    plt.grid(True)
    plt.ylabel('Values')
    plt.plot(values, '-', label='values')
    plt.legend(loc='upper right')


def doAtExit():
    serialArduino.close()
    print("Close serial")
    print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))


atexit.register(doAtExit)

print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))

for i in range(0, 200):
    values.append(0)

while True:
    while (serialArduino.inWaiting() == 0):
        pass
    print("readline()")
    valueRead = serialArduino.readline(500)

    try:
        valueInInt = int(valueRead)
        print(valueInInt)
        if valueInInt <= 1024:
            if valueInInt >= 0:

                values.append(valueInInt)
                values.pop(0)

                drawnow(plotValues)
            else:
                print("Invalid! negative number")
        else:
            print("Invalid! too large")
    except ValueError:
        print("Invalid! cannot cast")
