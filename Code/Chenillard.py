import smbus 
import time 
from gpio import * 
lp = [7,8,25,24] 
bp = 12 
seuil = [6400, 12800, 19200, 25600] 
offset = 8100 
 
def read_pot(address, CONFIG):
        bus.write_byte(address, CONFIG)
        data = bus.read_i2c_block_data(address, 0x00, 2)
        result = data[0]*256 + data[1]
        return data[0]*256+data[1]
 

 
 

    
    
for i in range(len(lp)): 
   closepin(lp[i]) 
   initpin(lp[i], "out") 
    
initpin(bp, "in") 
c = 0   
data = 0.05 
 
while 1: 
   time.sleep(0.1) 
   if readpin(bp) == False: 
      lp = lp[::-1] 
   setpin(lp[c%4-1], 0) 
   setpin(lp[c%4], 1) 
   c = c + 1 
   data = data + 1.5 
   time.sleep(data%3) 