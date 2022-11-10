import smbus
import time

def read_pot(address, CONFIG):
        bus.write_byte(address, CONFIG)
        data = bus.read_i2c_block_data(address, 0x00, 2)
        result = data[0]*256 + data[1]
        return data[0]*256+data[1]

if __name__ == "__main__":
    bus = smbus.SMBus(1)
    address = 0x68
    CONFIG = (0x10 | 0x08 | 0x00 | 0x40)

    while 1:
        value = read_pot(address, CONFIG)
        if value > 
