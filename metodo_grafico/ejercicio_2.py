import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def config():
    matplotlib.use('TkAgg')

def punto_dos():
    # Gráfica de los puntos intersección
    plt.plot(-1*5,5,'go',markersize=2)
    plt.plot(5,5,'go',markersize=2)
    plt.plot(5,-1*10,'go',markersize=2)
    plt.plot(-1*5,-1*10,'go',markersize=2)

    # Gráfica del área solución
    plt.fill([-1*5,5,5,-1*5,-1*5],[5,5,-1*10,-1*10,5],'g',alpha=0.75, label = 'Área solución')

    # Gráfica de la recta de la inecuación y de los ejes x e y

    plt.hlines(5,xmin = -5, xmax = 5,color = 'blue', label = 'y = 5')
    plt.hlines(0,xmin = -5, xmax = 5,color = 'black',linestyles = 'dashed')
    plt.vlines(0,ymin = -10, ymax = 10,color = 'black',linestyles = 'dashed')

    # Ajustes estéticos

    plt.legend()
    # Mostrar gráfica resultado

    plt.show()

if __name__ == '__main__':
    config()
    punto_dos()