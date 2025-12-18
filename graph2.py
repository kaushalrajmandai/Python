
import matplotlib.pyplot as plt
import numpy as np

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([248,250,260,270,280,290,300])
plt.plot(x,y)
plt.title("Test Plot")
plt.xlabel("average pulse")
plt.ylabel("calories burned")
plt.show()