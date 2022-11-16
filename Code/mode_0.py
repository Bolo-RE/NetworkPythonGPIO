import gpio     #import de la biblitohèque créée 

def mode_0():       #création de la fonction mode0
    while 1:        #loop infinie
        if gpio.readpin(12) == True:    #si le bouton poussoir est relâché, set la valeur du pin a 1
            gpio.setpin(24,1)           #la LED est eteinte
        else:
            gpio.setpin(24,0)   #si la condition n'est pas remplie par le booléen précedent, le BP est enfoncé
                                #la LED est donc allumée car pin_value vaut 0
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
    gpio.initpin(12,"in")       #initialisation des entrées/boutons poussoirs
    gpio.initpin(16,"in")
    gpio.initpin(20,"in")
    gpio.initpin(21,"in")
    gpio.initpin(7,"out")       #initialisation des sorties/LED
    gpio.initpin(8,"out")
    gpio.initpin(24,"out")
    gpio.initpin(25,"out")
    mode_0()
