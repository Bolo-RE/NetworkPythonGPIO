import gpio


def init():
    gpio.initpin(12, "in")  # initialisation des entrées
    gpio.initpin(16, "in")
    gpio.initpin(20, "in")
    gpio.initpin(21, "in")
    gpio.initpin(7, "out")  # initialisation des sorties
    gpio.initpin(8, "out")
    gpio.initpin(24, "out")
    gpio.initpin(25, "out")
    gpio.setpin(24, 1)
    gpio.setpin(25, 1)
    gpio.setpin(7, 1)
    gpio.setpin(8, 1)


def switchpin_no(led_pin_no, btn_pin_no):
    btn_status = gpio.readpin(btn_pin_no)  # obtient pin_value du bouton poussoir
    if gpio.readpin(led_pin_no):  # equivalent à 'if gpio.readpin(led_pin_no) == True
        gpio.setpin(led_pin_no, 0)  # set la valeur de la LED à 0 si pin_value vaut 1
    else:
        gpio.setpin(led_pin_no, 1)  # set la valeur de la LED à 1
    while btn_status == gpio.readpin(btn_pin_no):
        print("inverted !")


def mode_1():
    while 1:
        btn_status_12 = gpio.readpin(12)
        btn_status_16 = gpio.readpin(16)
        btn_status_20 = gpio.readpin(20)
        btn_status_21 = gpio.readpin(21)
        while (
            btn_status_12 == gpio.readpin(12)
            and btn_status_16 == gpio.readpin(16)
            and btn_status_20 == gpio.readpin(20)
            and btn_status_21 == gpio.readpin(21)
        ):
            print(
                "Attente..."
            )  # print 'Attente...' tant qu'aucune modification n'est effectuée/
            # qu'aucun bouton n'est utilisé
        if btn_status_12 != gpio.readpin(12):  # si pin_value du bouton change alors:
            switchpin_no(24, 12)  # on appelle la fonction switchpin_no() pour changer
            # la pin_value de la LED et ainsi l'allumer/éteindre
        if btn_status_16 != gpio.readpin(16):
            switchpin_no(25, 16)
        if btn_status_20 != gpio.readpin(20):
            switchpin_no(7, 20)
        if btn_status_21 != gpio.readpin(21):
            switchpin_no(8, 21)


def main():
    init()
    mode_1()  # appel de la fonction mode_1()


if __name__ == "__main__":
    main()
