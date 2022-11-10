import gpio

def mode_0():
    while 1:
        if gpio.readpin(12) == True:
            gpio.setpin(24,1)
        else:
            gpio.setpin(24,0)
        if gpio.readpin(16) == True:
            gpio.setpin(25,1)
        else:
            gpio.setpin(25,0)
        if gpio.readpin(20) == True:
            gpio.setpin(7,1)
        else:
            gpio.setpin(7,0)
        if gpio.readpin(21) == True:
            gpio.setpin(8,1)
        else:
            gpio.setpin(8,0)

if __name__ == "__main__":
    gpio.initpin(12,"in")
    gpio.initpin(16,"in")
    gpio.initpin(20,"in")
    gpio.initpin(21,"in")
    gpio.initpin(7,"out")
    gpio.initpin(8,"out")
    gpio.initpin(24,"out")
    gpio.initpin(25,"out")
    mode_0()
