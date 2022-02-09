# Sergio David Paez Suarez - 20191020167

#Importación de la libreria scipy
from scipy.optimize import  linprog
import math
#Si la función de desea maximizar como es el caso, debido a la limitante de scipy se deben realizar unas modificaciones
#a los datos a utilizar

# 1) Declaración de la funcion objetivo a minimizar o maximizar
"""En este caso se declara como una lista con los coeficientes de la función
Si se trata de maximización: declarar la función objetivo con los coeficientes opuestos"""

objective_function = [-21,-24,-36] # P = 21x + 24y + 36z

#Declarar restricciones

"""
Aclaración: Si la función es de maximizacion y alguna restriccion es >= (mayor o igual que)
tambien se deben invertir los coeficientes
"""

"""Se deben declarar por separado el lado izquierdo y derecho de las restricciones
El lazo izquierdo se declara como una matriz con los coeficientes de las tres restricciones
en cambio los valores independientes se ponen como un unico arreglo"""

left_side_restrictions = [
    [1,1,1],# x + y + z
    [1,1,2],# x + y + 2z
    [2,3,5] # 2x + 3y + 5z
]

right_side_restrictions = [400,500,1450]

solution = linprog(objective_function,left_side_restrictions,right_side_restrictions, method = 'simplex')

print("\n\t"+12*"-"+"Simplex Solution"+12*"-")
print("Objective function: P = 21x + 24y + 36z")
print("\nRestrictions:\n")
print("x + y + z <= 400")
print("x + y + zz <= 500")
print("2x + 3y + 5z <= 1450\n")
print("Success Operation: " + str(solution.success))
print("Optimization Value: "+str(int(math.fabs(solution.fun))))
print("Coordinates Optimal value: ("+str(int(solution.x[0])) + "," + str(int(solution.x[1]))+","
    +str(int(solution.x[2]))+")\n")