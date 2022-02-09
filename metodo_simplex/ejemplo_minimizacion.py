from scipy.optimize import  linprog
import math

# 1) Declaración de la funcion objetivo a minimizar o maximizar
"""En este caso se declara como una lista con los coeficientes de la función
Si se trata de maximización: declarar la función objetivo con los coeficientes opuestos"""

objective_function = [60000,100000] # P = 60000x + 100000y

#Declarar restricciones

"""
Aclaración: Si la función es de maximizacion y alguna restriccion es >= (mayor o igual que)
tambien se deben invertir los coeficientes
"""

"""Se deben declarar por separado el lado izquierdo y derecho de las restricciones
El lazo izquierdo se declara como una matriz con los coeficientes de las tres restricciones
en cambio los valores independientes se ponen como un unico arreglo"""

left_side_restrictions = [
    [-10,-25],# -10x - 25y
    [-12,-20]# -12x - 20y
]

right_side_restrictions = [-50,-50]

solution = linprog(objective_function,left_side_restrictions,right_side_restrictions, method = 'simplex')

print("\n\t"+12*"-"+"Simplex Solution"+12*"-")
print("Objective function: 60000x + 100000y")
print("\nRestrictions:\n")
print("10x + 25y >= 50")
print("12x + 20y >= 50\n")
print("Success Operation: " + str(solution.success))
print("Optimization Value: "+str(math.fabs(solution.fun)))
print("Coordinates Optimal value: ("+str((solution.x[0])) + "," + str(int(solution.x[1]))+")\n")