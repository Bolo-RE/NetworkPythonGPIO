def initpin(pin_no, pin_direction):
    try:
        fp1 = open("/sys/class/gpio/export","w")
        fp1.write(str(pin_no))
        fp1.close()
    except IOError:
       print("GPIO %s already Exists, so skipping export gpio" % (str(pin_no), ))

    gpioopnum = "gpio%s" % (str(pin_no), )
    pin1dir = open("/sys/class/gpio/"+gpioopnum+"/direction","w")
    pin1dir.write(pin_direction)
    pin1dir.close()

def setpin(pin_no, pin_value):
    gpioopnum = "gpio%s" % (str(pin_no), )
    pin1dir = open("/sys/class/gpio/"+gpioopnum+"/value","w")
    pin1dir.write(str(pin_value))
    pin1dir.close()


def readpin(pin_no):
    gpioopnum = "gpio%s" % (str(pin_no), )
    pin1val = open("/sys/class/gpio/"+gpioopnum+"/value","r")
    output = pin1val.read()
    pin1val.close()
    return output.startswith("1")


def closepin(pins):
    try:
        fp4 = open("/sys/class/gpio/unexport","w")
        fp4.write(str(pins))
        fp4.close()
    except IOError:
        print("GPIO %s is not found, so skipping unexport gpio" % (str(pins), ))
