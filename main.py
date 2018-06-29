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

levels = {
    1 : onionGpio.OnionGpio(5),
    2 : onionGpio.OnionGpio(4),
    3 : onionGpio.OnionGpio(19),
    4 : onionGpio.OnionGpio(18),
}

relays = {
    ('open' + WATER_RELAY) : onionGpio.OnionGpio(0),
    ('close' + WATER_RELAY) : onionGpio.OnionGpio(1),
    ('open' + STEAM_RELAY) : onionGpio.OnionGpio(45),
    ('close' + STEAM_RELAY) : onionGpio.OnionGpio(46),
    ('open' + GAS_RELAY) : onionGpio.OnionGpio(2),
    ('close' + GAS_RELAY) : onionGpio.OnionGpio(3)
}

def setup():
    for sensor in levels.itervalues():
        sensor.setInputDirection()

    for relay in relays.itervalues():
        relay.setOutputDirection(RELAY_OFF)

def getWaterLevel():
    # Setup serial port
    ser = serial.Serial(port='/dev/ttyS1', baudrate=9600, timeout=2)
    waterLevel = 0
        
    # Requests water level from Arduino
    ser.write("water_level")

    # Read 8 byte response
    waterLevel = ser.readAll()
    # ser.cancel_read()

    print("Level: " + waterLevel)
    return waterLevel

def setSolenoidState(relayName, state):
    # int(not value) inverts a integer (0/1)
    relays['close' + relayName].setValue(int(not state))
    relays['open' + relayName].setValue(state)

def main():
    setup()
    loop = 0

    while True:
        # 1-sec delay on the beggining of the loop just to decrease computational cost
        time.sleep(2)

        loop += 1
        print("\n Loop: " + str(loop))

        waterLevel = getWaterLevel()

        if waterLevel > 3:
            setSolenoidState(GAS_RELAY, RELAY_ON)

        if waterLevel < 4:
            setSolenoidState(WATER_RELAY, RELAY_ON)
        else:
            setSolenoidState(WATER_RELAY, RELAY_OFF)
            # if waterLevel == 5:
            #     setSolenoidState(GAS_RELAY, RELAY_OFF)

    return 0

def relayTest(relayStatus):
    print("Turning relays " + ("Off" if relayStatus else "On") + "...")

    for relay in relays.itervalues():
        relay.setValue(relayStatus)
        time.sleep(1)

if __name__ == '__main__':
    main()
