import numpy as np
from scipy import signal as sp
import matplotlib.pylab as plt

amplitud = 2
periodo = np.pi


t = np.arange(-1, 10, 0.001)
funcion = ((sp.square(2 * t)) * (amplitud / 2.0)) + (amplitud / 2.0)

plt.plot(t, funcion, lw=2)
plt.grid()
plt.annotate('Pi', xy = (np.pi, 1), xytext = (np.pi, 1.1))
plt.annotate('Pi/2', xy = (np.pi / 2.0, 1), xytext = (np.pi / 2.0, 1.1))
plt.ylabel('Amplitud')
plt.xlabel('Tiempo(t)')
plt.ylim(-1,2)
plt.xlim(-0.5, 4)
plt.show()
