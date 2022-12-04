# Example program to plot samples received from a serial connection to a pyplot grapf
import serial
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy

print("ctrl+c in terminal to abort")

# Will store all samples as we receive them
samples = []

plt.ion() # Required to allow us to update the plot as we receive new data

# Starts of with an empty plot
plot = plt.plot([], [])

# Our sample value range
plt.ylim(-50,500)

# Open serial connection
with serial.Serial("COM3", 9600, timeout=1) as connection:
    # Dumps any pre-buffered data
    connection.flush()

    # Initiate reading loop
    while True:
        # Read from serial port
        value_raw = connection.readline().strip().decode("utf-8")
        # Att! This conversion may fail if the value read is not number-like
        value = float(value_raw)
        # Add to set of samples
        samples.append(value_raw)

        # Plot sample set using matplotlib.pyplot
        plt.plot(range(0,len(samples)), samples, color="red")
        plt.pause(0.1) # gives us brief moments of time to interact with the UI
