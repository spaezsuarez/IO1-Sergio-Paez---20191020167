import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def config():
    matplotlib.use('TkAgg')

def f(x):
    return (60 - (2*x))/3

def punto_cinco():
    xr = np.linspace((-1*40),50)
    yr = f(xr)

    plt.plot(xr,yr,label='y > (x+2)/2')

    plt.hlines(0,xmin = -40, xmax = 50,color = 'blue', label = 'x > 0')


    plt.fill([0,0,30],[0,20,0],'g',alpha=0.75, label = 'Área solución')

    # Ajustes estéticos
    plt.legend()
    # Mostrar gráfica resultado
    plt.show()

if __name__ == '__main__':
    config()
    punto_cinco()

