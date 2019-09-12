import matplotlib.pyplot as plt
import math

# y = a * x + b
# x = [x for x in range(-1000,1000)]
# y = []
# a = 1
# for el in x:
#     temp = a * math.sin(el / 100* math.pi)
#     y.append(temp)

# plt.plot(x,y)
# plt.ylabel('y = a * sin(x)')
# plt.show()
# temp = a * math.sin(el * 1 *  math.pi / 1000 * 1000)

# for el in x:
#     temp = a * math.sin(el * 1 *  math.pi / 1000)
#     y.append(temp)

# plt.plot(x,y)
# plt.ylabel('y = a * sin(x)')
# plt.show()

import numpy as np
# import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r')
plt.show()