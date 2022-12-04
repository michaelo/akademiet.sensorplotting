# Minimal application to read from serial connection and print the results directly to the terminal
import serial

# Open serial connection. ATT: Rename serial-port according your system/setup
with serial.Serial("COM3", 9600, timeout=1) as connection:
    # Discards any pre-buffered data
    connection.flush()

    # Initiate reading loop
    print("ctrl+c to exit")
    while True:
        # Read from serial port
        value_raw = connection.readline().strip().decode("utf-8")
        value = float(value_raw)
        print(value) # debug
