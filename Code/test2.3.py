import gpio
import mode_0
import mode_1

if __name__ == "__main__":
    gpio.initpin(12,"in")   #initialisation des entrées
    gpio.initpin(16,"in")
    gpio.initpin(20,"in")
    gpio.initpin(21,"in")
    gpio.initpin(7,"out")   #initialisation des sorties
    gpio.initpin(8,"out")
    gpio.initpin(24,"out")
    gpio.initpin(25,"out")
    gpio.initpin(9,"in")
    gpio.setpin(24,1)   #extinction des LED
    gpio.setpin(25,1)
    gpio.setpin(7,1)
    gpio.setpin(8,1)
    choix = input("Quel mode (0 ou 1) : ")  #Demande à l'utilisateur quel mode utiliser
    if choix == "0":    #exécution du mode_O si l'input est 0
        mode_0.mode_0()
    elif choix == "1":  #exéctution du mode_1 si l'output est 1 
        mode_1.mode_1()
