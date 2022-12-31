# Método de diferencia dividida central para 
# diferenciación númerica

import numpy as np

# INGRESO
fx = lambda x: np.sqrt(x) * np.sin(x)

# tamano de paso
h = 0.005

# punto en el que queremos obtener el valor de la derivada.
xi = 5


# PROCEDIMIENTO
diffc = (-fx(xi+h*2)+8*fx(xi+h)-8*fx(xi-h)+fx(xi-h*2))/(12*h)
print('Respuesta = ',diffc)


# COMPROBACION CON COMANDO DERIVATIVE
from scipy.misc import derivative as diff
print('\nDerivada comando =',diff(fx,xi,dx=1e-6))
