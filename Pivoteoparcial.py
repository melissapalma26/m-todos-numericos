# Pivoteo parcial por filas
# Solución a Sistemas de Ecuaciones

import numpy as np

# INGRESO
A = np.array([[4,5,5],
              [2,2,8],
              [5,4,3]])

B = np.array([[60.70],
              [92.90],
              [56.30]])

# PROCEDIMIENTO

# Evitar truncamiento en operaciones
A = np.array(A,dtype=float) 

# Matriz aumentada
AB  = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)

# Pivoteo parcial por filas
tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]

for i in range(0,n-1,1):
    columna = abs(AB[i:,i])
    dondemax = np.argmax(columna)
    

    # intercambio de fila
    if (dondemax !=0):
        temporal = np.copy(AB[i,:])
        AB[i,:] = AB[dondemax + i,:]
        AB[dondemax + i,:] = temporal
        print('\ni=',i,'\n',AB)

AB1 = np.copy(AB)
print('\nMatriz original\n',AB0)
print('\nMatriz pivoteada\n',AB1)
        












    
