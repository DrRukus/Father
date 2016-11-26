#!/usr/bin/env python

import smbus
import time
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
I2C_ADDRESS = 0x04

EOL_ERROR = "unexpected EOF"

def writeNumber(value):
    bus.write_byte(I2C_ADDRESS, value)
    # bus.write_byte_data(I2C_ADDRESS, 0, value)
    return -1

def readNumber():
    number = bus.read_byte(I2C_ADDRESS)
    # number = bus.read_byte_data(I2C_ADDRESS, 1)
    return number

while True:
    try:
        var = input("Enter 1 - 9: ")
    except SyntaxError as err:
        if EOL_ERROR in str(err):
            print "Exiting..."
            exit(0)
        else:
            print err

    writeNumber(var)
    print "Value sent: {0}".format(var)
    # sleep one second
    time.sleep(0.1)

    number = readNumber()
    print "Value received: {0}".format(number)
    print
