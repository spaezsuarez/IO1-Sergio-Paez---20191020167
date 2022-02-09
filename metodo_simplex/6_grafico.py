# Sergio David Paez Suarez - 20191020167

#Importación de la libreria scipy
from scipy.optimize import  linprog
import math
#Si la función de desea maximizar como es el caso, debido a la limitante de scipy se deben realizar unas modificaciones
#a los datos a utilizar

# 1) Declaración de la funcion objetivo a minimizar o maximizar
"""En este caso se declara como una lista con los coeficientes de la función
Si se trata de maximización: declarar la función objetivo con los coeficientes opuestos"""

objective_function = [-4,-6] # P = 4x + 6y

#Declarar restricciones

"""
Aclaración: Si la función es de maximizacion y alguna restriccion es >= (mayor o igual que)
tambien se deben invertir los coeficientes
"""

"""Se deben declarar por separado el lado izquierdo y derecho de las restricciones
El lazo izquierdo se declara como una matriz con los coeficientes de las tres restricciones
en cambio los valores independientes se ponen como un unico arreglo"""

left_side_restrictions = [
    [2,1],# 2x + y
    [1,2],# x + 2y
    [1,1],# x + y
]

right_side_restrictions = [180,160,100]

solution = linprog(objective_function,left_side_restrictions,right_side_restrictions, method = 'simplex')

print("\n\t"+12*"-"+"Simplex Solution"+12*"-")
print("Objective function: p = 4x + 6y")
print("\nRestrictions:\n")
print("2x+2y <= 180")
print("x+2y <= 160")
print("x+y <= 100\n")
print("Success Operation: " + str(solution.success))
print("Optimization Value: "+str(int(math.fabs(solution.fun))))
print("Coordinates Optimal value: ("+str(int(solution.x[0])) + "," + str(int(solution.x[1]))+")\n")