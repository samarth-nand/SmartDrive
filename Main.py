import random
import time

class SmartDriveSystem:
    def __init__(self):
        pass

    def read_mock_sensor_data(self):
        """Simulates reading sensor data."""
        batteryLevel = random.randint(20, 100)  # Battery level in percentage
        milesLeft = random.uniform(10.0, 100.0)  # Miles left
        speed = random.uniform(0.0, 120.0)  # Speed in mph
        return batteryLevel, milesLeft, speed

    def process_sensor_data(self, batteryLevel, milesLeft, speed):
        """Processes the sensor data (in this simple example, just passes it through)."""
        return batteryLevel, milesLeft, speed

    def display_data(self, batteryLevel, milesLeft, speed):
        """Displays the data to the user."""
        print(f"Battery Level: {batteryLevel}%")
        print(f"Miles Left: {milesLeft:.2f} miles")
        print(f"Speed: {speed:.2f} mph")

    def run(self):
        """Main loop to run the system."""
        try:
            while True:
                # Read mock sensor data
                batteryLevel, milesLeft, speed = self.read_mock_sensor_data()
                
                # Process the data
                batteryLevel, milesLeft, speed = self.process_sensor_data(batteryLevel, milesLeft, speed)
                
                # Display the data
                self.display_data(batteryLevel, milesLeft, speed)
                
                # Wait for a bit before the next read
                time.sleep(2)  # Adjust as necessary
        except KeyboardInterrupt:
            print("SmartDrive System terminated by user.")

if __name__ == "__main__":
    smartDrive = SmartDriveSystem()
    smartDrive.run()
