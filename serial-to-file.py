# Application to read samples from a serial connection and store them to a file
# Somewhat complex example, but the critical parts are within the connect_and_dump-function
import serial
import sys
import signal

do_abort = False

def signal_handler(signum, frame):
    global do_abort
    do_abort = True

def connect_and_dump(device, baud, file_for_output):
    """
    Main logic: will connect to a serial port, and if successful open the specified output-file and start writing samples to it
    """
    print(f"Attempting to connect to serial device {device} at rate {baud}.")
    with serial.Serial(device, baud, timeout=1) as connection:
        connection.flush()

        print(f"Connection OK, opening output file {file_for_output} and starts reading from serial connection.")
        print("Att; a . will be printed each time data is read from the serial connection.")
        print("ctrl+c to exit.")

        # Open file for writing results to, and upon success initiate loop to read data from serial connection
        # Pre-existing contents of file will be cleared
        with open(file_for_output, "w") as f:
            while not do_abort:
                value = connection.readline().strip().decode("utf-8");
                f.write(value + "\n")
                f.flush() # Forces data to be written to file immediately
                print(".", end="", flush=True) # Debug-info; prints a "." to terminal to show that data is flowing

    print("\nGot exit-signal, so... exit it is!")

# Starting point of application
if __name__ == "__main__":
    # Setting up signal handler so we can gracefully exit if we receive e.g. a ctrl+c
    signal.signal(signal.SIGINT, signal_handler)

    if len(sys.argv) < 4:
        print("Required syntax:")
        print(f"{sys.argv[0]} device baud output-file")
        exit(-1)

    (_, device, baud, output_path) = sys.argv

    connect_and_dump(device, int(baud), output_path)
    # connect_and_dump('/dev/ttyS3', 9600, "results.txt")