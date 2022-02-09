# Modulos requeridos

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# Definición de las inecuación

def f1(x):
    return 180-2*x

def f2(x):
    return 80-(x/2)

def f3(x):
    return 100-x

def config():
    matplotlib.use('TkAgg')

def maximizar_funcion():
    # Definición de la variable independiente

    # Gráfica de los puntos intersección

    plt.plot(40,60,'go',color='red',markersize=10, label = 'Punto de optimización P(40,60)')
    plt.plot(80,20,'go',markersize=5)
    plt.fill([0,90,80,40,0,0],[0,0,20,60,80,0],'g',alpha=0.5, label = 'Área solución')

    # Valores de x a evaluar
    xr = np.linspace(-40,200,100)

    #Valores de y evaluandolo en cada una de las funciones
    y1r = f1(xr)
    y2r = f2(xr)
    y3r = f3(xr)

    # Gráfica de la recta de la inecuación y de los ejes x e y
    plt.plot(xr,y1r, label = 'y = 180-2*x')
    plt.plot(xr,y2r, label = 'y = 80-(x/2)')
    plt.plot(xr,y3r, label = 'y = 100-x')
    plt.vlines(0,ymin = -220, ymax = 220,color = 'black',linestyles = 'dashed')
    plt.hlines(0,xmin = -40, xmax = 200,color = 'black',linestyles = 'dashed')

    # Ajustes estéticos
    plt.grid(True, which='both')
    plt.legend()

    # Mostrar gráfica resultado
    plt.show()

if __name__ == '__main__':
    config()
    maximizar_funcion()