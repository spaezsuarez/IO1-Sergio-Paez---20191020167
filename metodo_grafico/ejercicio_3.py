import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def config():
    matplotlib.use('TkAgg')

def f(x):
    return (x+2)/2

def punto_tres():
    #Puntos en los cuales voy a evaluar la función para poder graficar
    xr = np.linspace(-1*12,10)
    #Valores de x evaluados en la función
    yr = f(xr)

    #Dibujando valores en el lienzo
    plt.plot(xr,yr,label='y > (x+2)/2')

    # Gráfica del área solución
    plt.fill([-12,-12,10,10],[-5,10,10,6],'g',alpha=0.75, label = 'Área solución')

    # Ajustes estéticos
    plt.legend()
    # Mostrar gráfica resultado
    plt.show()

if __name__ == '__main__':
    config()
    punto_tres()