# Método de Gauss-Seidel
# Método Iterativo para solución de sistemas de ecuaciones lineales

import numpy as np
import sys

# INGRESO
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

X0  = np.array([0.,0.,0.])

tol = 0.0000001
imax = 100

# Copiar matriz original para mostrar al final
B0 = np.transpose([B])
AB  = np.concatenate((A,B0),axis=1)
AB0 = np.copy(AB)

# PROCEDIMIENTO

tamano = np.shape(A)
n = tamano[0]
m = tamano[1]

#  valores iniciales
X = np.copy(X0)
diferencia = np.ones(n, dtype=float)
error = 2*tol

itera = 0
while not(error<=tol or itera>imax):
    # por fila
    for i in range(0,n,1):
        # por columna
        suma = 0 
        for j in range(0,m,1):
            # excepto diagonal de A
            if (i!=j): 
                suma = suma + A[i,j]*X[j]
        
        nuevo = (B[i] - suma)/A[i,i]
        diferencia[i] = np.abs(nuevo-X[i])
        X[i] = nuevo
    error = np.max(diferencia)

    # mostrar iteraciones
    print('\nIteración =',itera,', error= {:.6e}'.format(error))
    print(np.transpose([X]))
    #

    itera = itera + 1

    
# Respuesta X en columna
X = np.transpose([X])

# si NO converge
if (itera>imax):
    print('Método no converge')
    sys.exit()
    
# revisa respuesta
verify = np.dot(A,X)

# SALIDA
print('\nMatriz original')
print(AB0,'\n')
print('RESPUESTA:\n')
print('Solución X:')
print(X,'\n')
print('Verificación A.X=B:')
print(verify)
