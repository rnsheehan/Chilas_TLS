# Import various modules

import os
import sys
import glob
import re
import serial
import pyvisa
import time
import numpy
import math

# The aim of this script is to establish comms with the Chilas TLS
# R. Sheehan 13 - 11 - 2025

MOD_NAME_STR = "Chilas_Ctrl"

def Chils_Ctrl_Hacking():
    # Script for hacking through comms issues related to the Chilas TLS
    # FHP has already solved the major issues when he attempted to setup comms in LabVIEW
    # use the lessons learned here
    # R. Sheehan 13 - 11 - 2025
    
    FUNC_NAME = ".Chils_Ctrl_Hacking()" # use this in exception handling messages
    ERR_STATEMENT = "Error: " + MOD_NAME_STR + FUNC_NAME
    
    try:
        # start by attempting to set up a serial connection between the PC and the Chilas TLS
        
        # parameters to be passed to the serial open command
        ChilasPort = 'COM57' # this will have to be checked on your computer
        baudRate = 57600 # serial comms baud_rate
        readTimeout = 3 # timeout for reading data from the IBM4, units of second
        writeTimeout = 0.5 # timeout for writing data to the IBM4, units of second
        instr_obj = None # assign a default argument to the instrument object
        
        instr_obj = serial.Serial(port = ChilasPort, baudrate = baudRate, timeout = readTimeout, write_timeout = writeTimeout, stopbits = serial.STOPBITS_ONE, parity = serial.PARITY_NONE)
        
        # serial returns a boolean that can be used to test if the comms channel is open or not
        if instr_obj:
            # comms channel is open proceed

            # Both the following commands must execute successfully

            # Check that the comms link was established correctly
            instr_obj.write(b'CMDL?\r\n') # commands sent to the Chilas TLS must end with CR+LF = '\r\n'
            response = instr_obj.read_until('\n',size=None) # what should the response be? 
            print('\n',response)
        
            # Check that the comms link was established correctly
            instr_obj.write(b'*IDN?\r\n') # commands sent to the Chilas TLS must end with CR+LF = '\r\n'
            response = instr_obj.read_until('\n',size=None) # what should the response be? 
            print('\n',response)
        
            PLAY_WITH_LASER = False

            if PLAY_WITH_LASER:
                # Switch on the laser system Using the following command
                instr_obj.write(b'SYST:STAT 1\r\n') # commands sent to the Chilas TLS must end with CR+LF = '\r\n'
                response = instr_obj.read_until('\n',size=None) # what should the response be? 
                print('\n',response)
        
                # Once this command executes successfully, switch the laser on
                instr_obj.write(b'LSR:STAT 1\r\n') # commands sent to the Chilas TLS must end with CR+LF = '\r\n'
                response = instr_obj.read_until('\n',size=None) # what should the response be? 
                print('\n',response)
        
                # Set the laser current level
                instr_obj.write(b'LSR:ILEV 75.6\r\n') # commands sent to the Chilas TLS must end with CR+LF = '\r\n'
                response = instr_obj.read_until('\n',size=None) # what should the response be? 
                print('\n',response)
        
                # Set the uHeater voltage to change its phase
                instr_obj.write(b'DRV:D 0 3.5\r\n') # commands sent to the Chilas TLS must end with CR+LF = '\r\n'
                response = instr_obj.read_until('\n',size=None) # what should the response be? 
                print('\n',response)
            
                # Set the uHeater voltage to change its phase
                instr_obj.write(b'DRV:D 0 0.0\r\n') # commands sent to the Chilas TLS must end with CR+LF = '\r\n'
                response = instr_obj.read_until('\n',size=None) # what should the response be? 
                print('\n',response)
            
                # Set the laser current level
                instr_obj.write(b'LSR:ILEV 0.0\r\n') # commands sent to the Chilas TLS must end with CR+LF = '\r\n'
                response = instr_obj.read_until('\n',size=None) # what should the response be? 
                print('\n',response)

                # Switch the laser off
                instr_obj.write(b'LSR:STAT 0\r\n') # commands sent to the Chilas TLS must end with CR+LF = '\r\n'
                print('\n',response)
        
                # Swtich the system off
                instr_obj.write(b'SYST:STAT 0\r\n') # commands sent to the Chilas TLS must end with CR+LF = '\r\n'
                print('\n',response)

            # close the channel when it is no longer needed
            instr_obj.close()
        else:
            print('Could not open port:',ChilasPort)
            raise serial.SerialException
    except serial.SerialException as e:
        print(ERR_STATEMENT)
        print(e)        

def main():
    pass

if __name__ == '__main__':
    main()

    pwd = os.getcwd() # get current working directory

    print(pwd)
    
    Chils_Ctrl_Hacking()