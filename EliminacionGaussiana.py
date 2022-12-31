# Eliminación Gaussiana
# Solución a Sistemas de Ecuaciones de la forma A.X=B

import numpy as np

# INGRESO
# A = Matriz de coeficientes

A = np.array([[4,2,5],
              [2,5,8],
              [5,4,3]])

# B = Terminos independientes
B = np.array([[60.70],
              [92.90],
              [56.30]])


# Evitar truncamiento en operaciones
A = np.array(A,dtype=float) 

# PROCEDIMIENTO

# Matriz aumentada
AB  = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)

tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]


# Eliminación hacia adelante
for i in range(0,n-1,1):
    pivote   = AB[i,i]
    adelante = i + 1
        
    for k in range(adelante,n,1):
        factor  = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor    

# Sustitución hacia atrás
ultfila = n-1
ultcolumna = m-1
X = np.zeros(n,dtype=float)

for i in range(ultfila,-1,-1):
    suma = 0
    for j in range(i+1,ultcolumna,1):
        suma = suma + AB[i,j]*X[j]
        
    b = AB[i,ultcolumna]
    X[i] = (b-suma)/AB[i,i]

X = np.transpose([X])


# SALIDA - MOSTRAR RESULTADOS
print('\nMatriz aumentada:')
print(AB0)
print('\nEliminación hacia adelante')
print(AB)
print('\nRespuesta-solución: ')
print(X)
