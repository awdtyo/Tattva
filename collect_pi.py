import psutil
import time
import csv
import os

# Function to get Pi temperature directly from the system file
def get_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = int(f.read()) / 1000.0  # Convert millidegrees to Celsius
    return temp

output_file = "pi_thermal_data.csv"
file_exists = os.path.isfile(output_file)

with open(output_file, "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["timestamp", "cpu_usage", "cpu_freq", "ram_usage", "temp"])

    print("Logging data... Press Ctrl+C to stop.")
    try:
        while True:
            t = time.time()
            usage = psutil.cpu_percent(interval=1) # Measures over 1 second
            freq = psutil.cpu_freq().current
            ram = psutil.virtual_memory().percent
            temp = get_temp()
            
            writer.writerow([t, usage, freq, ram, temp])
            f.flush() # Forces writing to disk so data isn't lost
    except KeyboardInterrupt:
        print("\nLogging stopped.")
