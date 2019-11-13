import serial
import time
import os
import subprocess

os.system('sudo chnod 777 /dev/ttyAM0')
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
 
#gameA(色遊び)をarduinoに実行させる
def gameA():
    os.system('sudo chnod 777 /dev/ttyAM0')
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
    ser.write('a'.encode())
    flag = 'none'

    while(flag != 'A'.encode()):
        flag = ser.readline()
        time.sleep(2)
    
    ser.close()
    return

def gameB():
    os.system('sudo chnod 777 /dev/ttyAM0')
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
    ser.write('b'.encode())
    flag = 'none'

    while(flag != 'B'.encode()):
        flag = ser.readline()
        time.sleep(2)
    
    ser.close()
    return

def gameC():
    os.system('sudo chnod 777 /dev/ttyAM0')
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
    ser.write('c'.encode())
    flag = 'none'

    while(flag != 'C'.encode()):
        flag = ser.readline()
        time.sleep(2)
    
    ser.close()
    return

def gameD():
    os.system('sudo chnod 777 /dev/ttyAM0')
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
    ser.write('d'.encode())
    flag = 'none'

    while(flag != 'D'.encode()):
        flag = ser.readline()
        time.sleep(2)
    
    ser.close()
    return

def gameE():
    os.system('sudo chnod 777 /dev/ttyAM0')
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
    ser.write('e'.encode())
    flag = 'none'

    while(flag != 'E'.encode()):
        flag = ser.readline()
        time.sleep(2)
    
    ser.close()
    return

def gameF():
    os.system('sudo chnod 777 /dev/ttyAM0')
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10)
    ser.write('f'.encode())
    flag = 'none'

    while(flag != 'F'.encode()):
        flag = ser.readline()
        time.sleep(2)
    
    ser.close()
    return

time.sleep(10)
print("game start!!")
gameA()
print("Aが終わったよ")
gameB()
print("Bが終わったよ")
gameC()
print("Cが終わったよ")
gameD()
print("Dが終わったよ")
