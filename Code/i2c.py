import time

import smbus


def main():
    bus = smbus.SMBus(1)
    address = 0x68
    CONFIG = 0x10 | 0x00 | 0x00 | 0x40

    while 1:
        bus.write_byte(address, CONFIG)
        time.sleep(0.1)
        data = bus.read_i2c_block_data(address, 0x00, 2)
        result = data[0] * 256 + data[1]
        print(result)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
