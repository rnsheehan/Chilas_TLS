'''
Implementation of a class for interfacing to the Chilas TLS

R. Sheehan 13 - 11 - 2025
'''

# The laser in UCC is the Chilas-CT3
# More info on specs etc can be found here
# https://photonics.laser2000.co.uk/products/light-sources-safety/lasers/laser-diodes/ultra-narrow-linewidth-lasers/

import os
import sys
import glob
import re
import serial
import time
import numpy
import Sweep_Interval

# define the class for interfacing to the Chilas TLS
class Chilas_Iface(object):
    '''
    class for interfacing to the Chilas TLS
    '''
    
    # define the class constructor
    def __init__(self, port_name = None):
        '''
        constructor for the Chilas TLS class
        
        port_name is the name of the COM port to which the Chilas TLS is attached
        port_name = None => PC will search for 1st available Chilas TLS
        '''
        
        try:
            self.MOD_NAME_STR = "Chilas_Lib"
            self.FUNC_NAME = ".Chilas_Iface()" # use this in exception handling messages
            self.ERR_STATEMENT = "Error: " + self.MOD_NAME_STR + self.FUNC_NAME

            # parameters to be passed to the serial open command
            self.baud_rate = 9600 # serial comms baud_rate
            self.read_timeout = 3 # timeout for reading data from the IBM4, units of second
            self.write_timeout = 0.5 # timeout for writing data to the IBM4, units of second
            self.instr_obj = None # assign a default argument to the instrument object

            # identify the port name
            if port_name is not None:
                self.ChilasPort = port_name # string containing the port no. of the device
            else:
                self.FindChilas() # find the Chilas port attached to the PC
                
            # open the serial comms link to port_name
            self.OpenComms()
        except TypeError as e:
            print(self.ERR_STATEMENT)
            print(e)
        except serial.SerialException as e:
            print(self.ERR_STATEMENT)
            print(e)
            
    # destructor  
    # https://www.geeksforgeeks.org/destructors-in-python/          
    def __del__(self):
        """
        close the link to the instrument object when it goes out of scope
        """
        
        if self.ChilasPort is not None and self.instr_obj.isOpen():
            # close the link to the instrument object when it goes out of scope
            print('Closing Serial link with:',self.instr_obj.name)
            self.ZeroChilas()
            self.instr_obj.close()
        else:
            # Do nothing, no link to IBM4 established
            pass
            
    def __str__(self):
        """
        return a string the describes the class
        """
        
        return "class for interfacing to Chilas TLS"
    
    def CommsStatus(self):
        """
        investigate the status of the serial comms link
        """
        
        if self.ChilasPort is not None and self.instr_obj.isOpen():
            print('Communication with:',self.instr_obj.name,' is open')
            return True
        else:
            print('Communication with: Chilas TLS is not open')
            return False

    def OpenComms():
        pass
    
    def ZeroChilas():
        pass
    
    def FindChilas():
        pass
    
    def SetLasCurrLev(self, laser_current = 0.0):
        pass
    
    def SetPhase(self, chn_no = 0, phase_voltage = 0.0):
        pass