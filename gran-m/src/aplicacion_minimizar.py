# Sergio David Paez Suarez - 20191020167

#Importación de la libreria scipy
from scipy.optimize import  linprog
import math
#Si la función de desea maximizar como es el caso, debido a la limitante de scipy se deben realizar unas modificaciones
#a los datos a utilizar

# 1) Declaración de la funcion objetivo a minimizar o maximizar
"""En este caso se declara como una lista con los coeficientes de la función
Si se trata de maximización: declarar la función objetivo con los coeficientes opuestos"""

objective_function = [1/4,2/3,0] # P = -x1 -x2 - x3

#Declarar restricciones

"""
Aclaración: Si la función es de maximizacion y alguna restriccion es >= (mayor o igual que)
tambien se deben invertir los coeficientes
"""

"""Se deben declarar por separado el lado izquierdo y derecho de las restricciones
El lazo izquierdo se declara como una matriz con los coeficientes de las tres restricciones
en cambio los valores independientes se ponen como un unico arreglo"""

inecuations_left_side_restrictions = [
    [1/2,1/4,2],# x1 + x2
]

inecuations_right_side_restrictions = [1000000]

"""Ademas de esto se debe tener en cuenta que si hay alguna restriccion con un igual (=)
   Se tiene que pasar en un arreglos aparte, pero igualmente representando el lado derecho e izquierdo de la igualdad
"""

equations_left_side_restriction = [
    [1,1,1]
]

equations_right_restriction = [3300000]


solution = linprog(
    objective_function,
    inecuations_left_side_restrictions,
    inecuations_right_side_restrictions,
    equations_left_side_restriction,
    equations_right_restriction,
    method = 'simplex'
)

print("\n\t"+12*"-"+"Solution"+12*"-")
print("Optimization Value: "+str(int(math.fabs(solution.fun))))
print("Coordinates Optimal value: ("+str(solution.x)+")\n")