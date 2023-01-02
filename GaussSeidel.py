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


B = np.array([97, -1, -22, 138, 62])

X0  = np.array([0.,0.,0.,0.,0])

tol = 0.0000001
imax = 100

# Copiar matriz original para mostrar al final
B0 = np.transpose([B])
AB  = np.concatenate((A,B0),axis=1)
print(AB)
AB0 = np.copy(AB)

# PROCEDIMIENTO

tamano = np.shape(A)
n = tamano[0]
m = tamano[1]

# Pivoteo

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

#---------------------------------

# Separar A y B de la matriz


M = np.array(AB1[:,0])
N = np.array(AB1[:,1])
P = np.array(AB1[:,2])
R = np.array(AB1[:,3])
S = np.array(AB1[:,4])

ZA1 = np.array([M, N, P, R, S])
ZA = np.transpose(ZA1)

A = np.array(ZA)
print(A)

B = np.array(AB1[:,5])
print(B)

#  valores iniciales
X = np.copy(X0)
print(X)
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
print('\nMatriz aumentada:')
print(AB0)
print('\nMatriz pivoteada:\n')
print(AB1)
print('RESPUESTA:\n')
print('Solución X:')
print(X,'\n')
print('Verificación A.X=B:')
print(verify)
