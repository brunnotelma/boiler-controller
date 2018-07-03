#define LEVEL_1 8
#define LEVEL_2 9
#define LEVEL_3 10
#define LEVEL_4 11
#define LEVEL_5 12

void setup() {
    // Set all level sensors` pinMode to INPUT
    pinMode(LEVEL_1, INPUT);
    pinMode(LEVEL_2, INPUT);
    pinMode(LEVEL_3, INPUT);
    pinMode(LEVEL_4, INPUT);
    pinMode(LEVEL_5, INPUT);

    // Start Serial communication
    Serial.begin(9600);
}

// Temp string to hold serial content
String readSerial;

// Declare all possible water levels
int levels[] = {
    LEVEL_1,
    LEVEL_2,
    LEVEL_3,
    LEVEL_4,
    LEVEL_5,
};

void loop() {
    // Wait 100ms
    delay(100);

    // Check if there is data available
    if (Serial.available() > 0) {
        // Reads the data coming from Serial
        readSerial = Serial.readString();
        // Trims its data, removing trailing line feeds
        readSerial.trim();

        if (readSerial == "water_temperature") {
            // Read water temperature and sends through Serial (RX/TX)
            Serial.print("60");
        }else if(readSerial == "steam_temperature"){
            // Read steam temperature and sends through Serial (RX/TX)
            Serial.print("75");
        }else if(readSerial == "water_level"){
            // Read water level and sends through Serial (RX/TX)
            Serial.print(getWaterLevel());
        }
    }
}

int getWaterLevel() {
    int water_level = 0;

    // For each sensor, reads the input
    for(int i = 0; i < 5; i++) {
        delay(100);
        
        // If the value is HIGH, it means that 
        // the sensor has water on it.
        if(digitalRead(levels[i]) == HIGH){
            // Store the level number
            // P.S: The (+1) thing is to get the number on a 1-5 scale
            // instead of the 0-4 scale which the array index is
            water_level = i + 1;
        }
    }

    return water_level;
}
