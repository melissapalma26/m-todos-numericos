# Eliminación Gaussiana
# Solución a Sistemas de Ecuaciones de la forma A.X=B

import numpy as np

# INGRESO
# A = Matriz de coeficientes

A= np.array([[-4, -1, -2, 3, 7],
             [6, -7, 4, 5, 1],
             [9, 7, 2, -3, 10],
             [-10, -10, 8, -2, 2],
             [-7, 10, -3, -4, 4]])


B = np.array([[97],
              [-1],
              [-22],
              [138],
              [62]])


# Evitar truncamiento en operaciones
A = np.array(A,dtype=float) 
B = np.array(B,dtype=float) 

# PROCEDIMIENTO

# Matriz aumentada
AB  = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)

#pivoteo
#------------------------------------------------------------------------------------------------------------------
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
#print('\nMatriz original\n',AB0)
#print('\nMatriz pivoteada\n',AB1)

#procedimiento de eliminacion 
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
print('\nMatriz pivoteada:\n')
print(AB1)
print('\nEliminación hacia adelante')
print(AB)
print('\nRespuesta-solución: ')
print(X)
