import matplotlib.pyplot as plt
import numpy as np

x = np.array([6,7,8,9,10,11,12,13,14,15,16,17,18])
y = np.array([22,24,25,27,30,33,37,38,30,28,28,27,24])
y1= np.array([23,25,26,27,30,32,35,40,42,38,37,34,34])
plt.plot(x, y,marker='x')
plt.plot(x, y1,marker='o')
plt.legend(['29 June, 2023','29 May,2023'])
plt.xlabel("Time")
plt.ylabel("Celsius")
plt.title("Temperature")
plt.grid(True)
plt.show()
