import gpio
import mode_0
import mode_1

if __name__ == "__main__":
    gpio.initpin(12,"in")
    gpio.initpin(16,"in")
    gpio.initpin(20,"in")
    gpio.initpin(21,"in")
    gpio.initpin(7,"out")
    gpio.initpin(8,"out")
    gpio.initpin(24,"out")
    gpio.initpin(25,"out")
    gpio.initpin(9,"in")
    gpio.setpin(24,1)
    gpio.setpin(25,1)
    gpio.setpin(7,1)
    gpio.setpin(8,1)
    choix = input("Quel mode (0 ou 1) : ")
    if choix == "0":
        mode_0.mode_0()
    elif choix == "1":
        mode_1.mode_1()
