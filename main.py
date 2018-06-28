import onionGpio
import time

rele1 = onionGpio.OnionGpio(0)

# nivel1 = onionGpio.OnionGpio(0)
# nivel2 = onionGpio.OnionGpio(1)
# nivel3 = onionGpio.OnionGpio(6)
# nivel4 = onionGpio.OnionGpio(7)
# nivel5 = onionGpio.OnionGpio(8)

def setup():
    rele1.setOutputDirection()

# def verificarNivel():


def main():
    setup()
    nivel = 0

    while True:
        rele1.setValue(1)
        time.sleep(1)
        rele1.setValue(0)

        # nivel = verificarNivel()

        # if nivel == 1:

        # elif nivel == 2:

        # elif nivel == 3:

        # elif nivel == 4:

        # elif nivel == 5:



if __name__ == '__main__':
    main()