# Metodo trapecio para integración

import numpy as np

# INGRESO

fx = lambda x: x * np.sin(x)

# limites de integral

a = 1
b = 2

# numero de subintervalos

n = 5

# PROCEDIMIENTO

suma = 0

for i in range(0,n,1):
    h = (b - a)/n
    area = (h/2) * ( (fx(a + (i*h))) + (fx(a + ((i+1)*h))))
    suma = suma + area
    
print('\nEl valor de la integral en los limites: ')
print('a=',a)
print('b=',b)
print('con n=',n, 'subintervalos')
print('es:',suma)
