import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def config():
    matplotlib.use('TkAgg')

#Función que representa la primera inecuación
def f1(x):
    return 3 - (2*x)

#Función que representa la segunda inecuación
def f2(x):
    return x

def punto_cuatro():
    # Gráfica de los puntos intersección
    xr1 = np.linspace(-1*5,5)
    yr1 = f1(xr1)
    plt.plot(xr1,yr1,label='y > 3 - 2x')

    xr2 = np.linspace(-5,5)
    yr2 = f2(xr2)
    plt.plot(xr2,yr2,label='y <= x')

    #dibujado recta contante y = 1/2
    plt.hlines(1/2,xmin = -5, xmax = 5,color = 'green', label = 'y > 1/2')

    #Puntos de intersección de las rectas
    plt.plot(1,1,'go',markersize=5)
    plt.plot(0.5,0.5,'go',markersize=5)
    plt.plot(1.2,0.5,'go',markersize=5)

    # Gráfica del área solución
    plt.fill([0.5,1,1.2],[0.5,1,0.5],'r',alpha=0.75, label = 'Área solución')

    plt.legend()
    # Mostrar gráfica resultado

    plt.show()

if __name__ == '__main__':
    config()
    punto_cuatro()