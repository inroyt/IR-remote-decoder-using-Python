# A program to decode NEC IR remote keys using MicroPython based embedded development boards( This code was tested on a Raspberry Pi Pico)
#visit->  https://techdocs.altium.com/display/FPGA/NEC+Infrared+Transmission+Protocol   for information about NEC Infrared Transmission Protocol
# See the messeage frame of the protocol for better understanding of the code
from machine import Pin                           
import math
import utime
import machine
input=Pin(18,Pin.IN)                      #input from 38KHz IR sensor
output=Pin(25, Pin.OUT)                   #A LED as test output
count=0
while True:
    value=1
    while value:                          #Loop until a 0 is detected
        value=input.value()
    start=utime.ticks_us()                #Set the start time of the command
    command=[]                            #To buffer the command pulses
    numOnes=0
    previous=0                            #Keep track of transitions from 1 to 0
    while True:
        if value != previous:
            end=utime.ticks_us()
            pulselen=end-start
            start=end
            command.append((previous,pulselen))
        if value:
            numOnes+=1
        else:
            numOnes=0
        if numOnes>10000:
            break
        previous=value
        value=input.value()
    print ("******START******")
    for (value,pulselen) in command:
         print (value,pulselen)
    print ("****END****\n")
    print ("size of array is"+str(len(command)))
    binaryString = "".join(map(lambda x: "1" if x[1] > 1000 else "0", filter(lambda x: x[0] == 1, command)))     #Binary value of the pressed key
    print(binaryString)
    if binaryString=="10000000111111110111110000000011111":          #To toggle the LED 
        output.on()
        count+=1
    if count>1:
        output.off()
        count=0
    
   

    
        
        
    
    
            
            
            
        
        
