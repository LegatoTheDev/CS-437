from sense_hat import SenseHat
from matplotlib import pyplot as plt
import time
import numpy as np
sense = SenseHat()

temps = []

for i in range(20):
    new_t = sense.get_temperature()
    time.sleep(0.2)
    temps.append(new_t)

avg_temp = []
raw_temp = []
samples = 100
for i in range(samples):
    reading = sense.get_temperature()
    temps.pop(0)
    temps.append(reading)
    avg_temp.append(np.array(temps).mean())
    raw_temp.append(reading)
    time.sleep(0.2)
plt.plot([i for i in range(samples)] , avg_temp)
plt.plot([i for i in range(samples)] , raw_temp)
plt.show()


