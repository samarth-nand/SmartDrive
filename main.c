// main.c
#include "sensor.h"
#include "display.h"
#include <stdio.h>
#include <stdlib.h> // For srand()
#include <time.h>   // For time()

int main() {
    srand(time(NULL)); // Seed the random number generator
    
    while (1) {
        SensorData data = readSensorData();
        data = processSensorData(data);
        displayData(data);

        // Pause for demonstration purposes
        printf("Press Enter to refresh...\n");
        while (getchar() != '\n');
    }

    return 0;
}
