import time

import gpio
import smbus


def read_pot(bus, address, CONFIG):
    bus.write_byte(address, CONFIG)
    time.sleep(0.1)
    data = bus.read_i2c_block_data(address, 0x00, 2)
    return data[0] * 256 + data[1]


def get_waiting_time(pot):
    if pot < 0.05:
        pot = 0.05
    return pot % 3


def mode_chenille(bus, address, CONFIG, lp, bp):
    state = [0, 1, 1, 1]  # Si besoin on peut changer l'affichage
    offset = 0  # Permet le décalage de state pour chaque lumière
    fwd = True  # Booléen indiquant le sens de la chenille
    while True:
        while gpio.readpin(bp) is True:  # Tant que le bouton est relaché
            offset = (offset + (1 if fwd else -1)) % len(state)  # On décale l'offset
            for i in range(len(lp)):  # Pour toutes les led
                gpio.setpin(
                    lp[i], state[(i + offset) % len(state)]
                )  # On met la bonne valeur en fonction de state et offset
            time.sleep(
                get_waiting_time(read_pot(bus, address, CONFIG))
            )  # On attend le temps qu'il faut indiqué par le potentionmètre
        fwd = not fwd  # On inverse le sens
        while gpio.readpin(bp) is False:  # Tant que le bouton est enfoncé
            offset = (offset + (1 if fwd else -1)) % len(state)
            for i in range(len(lp)):
                gpio.setpin(lp[i], state[(i + offset) % len(state)])
            time.sleep(get_waiting_time(read_pot(bus, address, CONFIG)))
        # Donc le deuxième while sert d'anti rebond


def light_threshold(pot, seuil, lp):

    if pot > seuil[3]:  # Tout est allumé
        for i in range(4):
            gpio.setpin(lp[i], 0)

    elif pot > seuil[2]:  # Tout sauf la dernière
        for i in range(3):
            gpio.setpin(lp[i], 0)
        gpio.setpin(lp[3], 1)

    elif pot > seuil[1]:  # Les deux premières led sont allumées
        for i in range(2):
            gpio.setpin(lp[i], 0)
        for i in range(2):
            gpio.setpin(lp[4 - i], 1)

    elif pot > seuil[0]:  # La première est allumée seulement
        gpio.setpin(lp[0], 0)
        for i in range(3):
            gpio.setpin(lp[4 - i], 1)

    else:  # Aucunes n'est allumée
        for i in range(4):
            gpio.setpin(lp[i], 1)

    return


def mode_light_threshold(bus, address, CONFIG, lp):
    seuil = [6553, 13107, 26214, 39321]
    while True:
        light_threshold(read_pot(bus, address, CONFIG), seuil, lp)
        time.sleep(0.1)


def main():
    bus = smbus.SMBus(1)
    address = 0x68
    CONFIG = 0x10 | 0x00 | 0x00 | 0x40

    lp = [7, 8, 25, 24]
    bp = 12

    gpio.closepin(bp)
    gpio.initpin(bp, "in")

    for i in range(len(lp)):
        gpio.closepin(lp[i])
        gpio.initpin(lp[i], "out")

    if input("Mode seuil (1) ou mode chenille (2) : ") == "1":
        mode_light_threshold(bus, address, CONFIG, lp)
    else:
        mode_chenille(bus, address, CONFIG, lp, bp)


if __name__ == "__main__":
    main()
