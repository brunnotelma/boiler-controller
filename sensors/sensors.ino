#define LEVEL_1 9
#define LEVEL_2 10
#define LEVEL_3 11
#define LEVEL_4 12

void setup() {
    pinMode(LEVEL_1, INPUT);
    pinMode(LEVEL_2, INPUT);
    pinMode(LEVEL_3, INPUT);
    pinMode(LEVEL_4, INPUT);

    Serial.begin(9600);
}

String readSerial;
int levels[] = {
    LEVEL_1,
    LEVEL_2,
    LEVEL_3,
    LEVEL_4,
};

void loop() {
    delay(50);

    // Wait until there is data available
    if (Serial.available() > 0) {
        readSerial = Serial.readString();
        readSerial.trim();

        if (readSerial == "water_temperature") {
            // Read water temperature and sends through Serial (RX/TX)
            Serial.println("60");
        }else if(readSerial == "steam_temperature"){
            // Read steam temperature and sends through Serial (RX/TX)
            Serial.println("75");
        }else if(readSerial == "water_level"){
            // Read water level and sends through Serial (RX/TX)
            Serial.println(getWaterLevel());
        }
    }
}

int getWaterLevel() {
    int water_level = 0;

    for(int i = 0; i < 4; i++) {
        delay(50);
        
        if(digitalRead(levels[i]) == HIGH){
            water_level = i + 1;
        }
    }

    return water_level;
}
