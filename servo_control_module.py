
import serial
import time

class ServoControlModule:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):
        try:
            self.serial_connection = serial.Serial(port, baudrate, timeout=1)
            time.sleep(2)  # Wait for the connection to establish
        except Exception as e:
            raise RuntimeError(f"Failed to initialize serial connection: {str(e)}")
        
    def execute(self, commands):
        responses = []
        try:
            for servo, angle in commands.items():
                command = f"{servo} {angle}\n"
                self.serial_connection.write(command.encode('utf-8'))
                response = self.serial_connection.readline().decode('utf-8').strip()
                responses.append(response)
        except Exception as e:
            responses.append(f"Error executing servo command: {str(e)}")
        return responses

    def close(self):
        try:
            self.serial_connection.close()
        except Exception as e:
            raise RuntimeError(f"Failed to close serial connection: {str(e)}")
