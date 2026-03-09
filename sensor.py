import random
import time

for i in range(5):
    voltage = round(random.uniform(0.0, 5.0), 2)
    print(f"Voltage reading: {voltage} V")
    time.sleep(1)
