import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0, 2*np.pi, 0.1)
y=np.sin(x)
n=60
rangi=plt.cm.jet(np.linspace(1, 0, n))
for i in range(n):
    plt.plot(x, y*i, color=rangi[i])

plt.show()
    



