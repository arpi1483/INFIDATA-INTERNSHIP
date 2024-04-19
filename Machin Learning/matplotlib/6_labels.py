import matplotlib.pyplot as plt
import numpy as np

x=np.array([3,5,6,7])
y=np.array([7,8,6,5])

plt.plot(x,y)
plt.xlabel("average pluse")
plt.ylabel("calories burn")
plt.title('sports watch data')

plt.show()