from scipy.optimize import linprog
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def minimizar():
    #Coeficientes de la función a minimizar
    c_f = [1000,2000]

    #Matriz de coeficientes de las restricciones de la fgunción
    restricciones = [[2,-1],[2,1],[1,0],[0,1]]

    #Arreglo con los valores independientes de las restricciones
    coeficientes_restricciones = [0,4,6,4]

    response = linprog(c_f,restricciones,coeficientes_restricciones)

    print(response.fun)
    print("x: " + str(response.x[0]) + " ,y: " + str(response.x[1]))

# Definición de las inecuación

def config():
    matplotlib.use('TkAgg')

def f1(x):
    return 2*x

def f2(x):
    return (4 - (2*x))

def minimizar_ejemplo():
    plt.plot(2,0,'go',color='red',markersize=10, label = 'Punto de optimización P(2,0)')

    xr1 = np.linspace(0,6)
    yr1 = f1(xr1)
    plt.plot(xr1,yr1,label='y <= 2x')

    xr2 = np.linspace(0,4.5)
    yr2 = f2(xr2)
    plt.plot(xr2,yr2,label='y > 4 - 2x')

    plt.hlines(4,xmin = 0, xmax = 6,color = 'green', label = 'y = 4')
    plt.hlines(0,xmin = 0, xmax = 6,color = 'black')

    plt.axvline(x=6, ymin=0, ymax=6, label = 'x = 6')

    plt.fill([1,2,6,6,2],[2,4,4,0,0],'y',alpha=0.5, label = 'Área solución')

    plt.legend()
    plt.show()

if __name__ == '__main__':
    config()
    minimizar()
    minimizar_ejemplo()