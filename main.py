import serial
import onionGpio
import time

# Relay states
RELAY_ON = 0
RELAY_OFF = 1

# Relay names
WATER_RELAY = 'Water'
STEAM_RELAY = 'Steam'
GAS_RELAY = 'Gas'

relays = {
    ('open' + WATER_RELAY) : onionGpio.OnionGpio(0),
    ('close' + WATER_RELAY) : onionGpio.OnionGpio(1),
    ('open' + STEAM_RELAY) : onionGpio.OnionGpio(19),
    ('close' + STEAM_RELAY) : onionGpio.OnionGpio(18),
    ('open' + GAS_RELAY) : onionGpio.OnionGpio(2),
    ('close' + GAS_RELAY) : onionGpio.OnionGpio(3)
}

def setup():
    # For each relay pin, set its GPIO to output and state = 1
    for relay in relays.itervalues():
        relay.setOutputDirection(RELAY_OFF)

def getWaterLevel():
    waterLevel = ""

    # Keeps in the loop while value received is not valid
    while(not isInt(waterLevel)):
        ser = serial.Serial(port='/dev/ttyS1', baudrate=9600, timeout=2)
	# Requests water level from Arduino
        ser.write("water_level")
        # Read 8 byte response
        waterLevel = ser.read(8)
        # Closes communication port
        ser.cancel_read()

    return int(waterLevel)

# Sets relay state, based on its name
def setSolenoidState(relayName, state):
    # int(not value) inverts a integer (0/1)
    relays['close' + relayName].setValue(int(not state))
    relays['open' + relayName].setValue(state)

def main():
    setup()

    while True:
        # 100ms delay on the beggining of the loop just to decrease computational cost
        time.sleep(0.1)

        waterLevel = getWaterLevel()
        print("Level: " + str(waterLevel))

        if waterLevel < 4:
            setSolenoidState(STEAM_RELAY, RELAY_OFF)
            setSolenoidState(WATER_RELAY, RELAY_ON)

            if waterLevel < 2 :
                setSolenoidState(GAS_RELAY, RELAY_OFF)
            else:
                setSolenoidState(GAS_RELAY, RELAY_ON)
        else:
            setSolenoidState(WATER_RELAY, RELAY_OFF)
            if waterLevel == 5:
                setSolenoidState(STEAM_RELAY, RELAY_ON)
                setSolenoidState(GAS_RELAY, RELAY_OFF)
            else:
                setSolenoidState(GAS_RELAY, RELAY_ON)

    return 0

# Checks if string content is an integer
def isInt(string):
    try: 
        int(string)
        return True
    except ValueError:
        return False

# Test all relays, turning them on and off based on the param `relayStatus`
def relayTest(relayStatus):
    print("Turning relays " + ("Off" if relayStatus else "On") + "...")

    for relay in relays.itervalues():
        relay.setValue(relayStatus)
        time.sleep(1)

if __name__ == '__main__':
    main()
