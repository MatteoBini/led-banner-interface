import serial


class Banner:
    # Configure the serial port settings
    __port = '/dev/rfcomm5'  # Virtual serial port associated with the Bluetooth device
    __baudrate = 9600  # Replace with the appropriate baud rate

    def send(self, msg) -> bool:

        try:
            # Open the serial port
            serial_port = serial.Serial(self.__port, self.__baudrate)

            # Check if the port is open
            if serial_port.is_open:
                print(f"Serial port {self.__port} opened successfully.")

            # Send data over the serial port
            data = msg + "\n"
            serial_port.write(data.encode("UTF-8"))

            # Close the serial port
            serial_port.close()
        except serial.SerialException as e:
            return True
