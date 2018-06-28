import onionGpio
import time

reles = {
    0 : onionGpio.OnionGpio(0)
    1 : onionGpio.OnionGpio(1)
    2 : onionGpio.OnionGpio(19)
    3 : onionGpio.OnionGpio(18)
    4 : onionGpio.OnionGpio(2)
    5 : onionGpio.OnionGpio(3)
}

def setup():
    for rele in reles.itervalues():
        rele.setOutputDirection(0)

def main():
    setup()
    releStatus = 1

    while 1:
        print("Ligando reles..." if releStatus else "Desligando reles...")

        for rele in reles.itervalues():
            rele.setValue(releStatus)
            time.sleep(1)

        releStatus = int(not releStatus)

if __name__ == '__main__':
    main()
