import onionGpio
import time

rele1 = onionGpio.OnionGpio(0)
rele2 = onionGpio.OnionGpio(1)
rele3 = onionGpio.OnionGpio(19)
rele4 = onionGpio.OnionGpio(18)
rele5 = onionGpio.OnionGpio(2)
rele6 = onionGpio.OnionGpio(3)

def setup():
    rele1.setOutputDirection(0)
    rele2.setOutputDirection(0)
    rele3.setOutputDirection(0)
    rele4.setOutputDirection(0)
    rele5.setOutputDirection(0)
    rele6.setOutputDirection(0)

def main():
    setup()
    releStatus = 1

    while 1:
        print("Ligando reles..." if releStatus == 1 else "Desligando reles...")

	rele1.setValue(releStatus)
        time.sleep(1)
        
	rele2.setValue(releStatus)
	time.sleep(1)

	rele3.setValue(releStatus)
        time.sleep(1)

	rele4.setValue(releStatus)
        time.sleep(1)

	rele5.setValue(releStatus)
	time.sleep(1)

	rele6.setValue(releStatus)
	time.sleep(1)

	releStatus = int(not releStatus)

if __name__ == '__main__':
    main()
