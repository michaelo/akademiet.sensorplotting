import serial
import sys
import signal

do_abort = False

def signal_handler(signum, frame):
    global do_abort
    do_abort = True

def connect_and_dump(device, baud, file_for_output, clear_file=True):
    """
    Main logic: will connect to a serial port, and if successful open the specified output-file and start writing samples to it
    """
    print(f"Attempting to connect to serial device {device} at rate {baud}.")
    connection = serial.Serial(device, baud, timeout=1)

    print(f"Connection OK, opening output file {file_for_output} and starts reading from serial connection.")
    print("Att; a . will be printed each time data is read from the serial connection.")
    print("ctrl+c to exit.")

    # Open file for writing results to, and upon success initiate loop to read data from serial connection
    with open(file_for_output, "w" if clear_file else "a") as f:
        while not do_abort:
            f.write(connection.readline().strip().decode("utf-8") + "\n")
            print(".", end="", flush=True)
            f.flush()

    print("\nGot exit-signal, so... exit it is!")


if __name__ == "__main__":
    # Setting up signal handler so we can gracefully exit if we receive e.g. a ctrl+c
    signal.signal(signal.SIGINT, signal_handler)

    connect_and_dump('/dev/ttyS3', 9600, "results.txt", clear_file=True)