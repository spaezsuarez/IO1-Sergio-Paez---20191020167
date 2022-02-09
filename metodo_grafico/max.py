import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Definición de las inecuación

def config():
    matplotlib.use('TkAgg')

def f1(x):
    return (750-x)/1.5

def f2(x):
    return 750-(1.5*x)

def maximizar_ejemplo():
    plt.plot(300,300,'go',color='red',markersize=10, label = 'Punto de optimización P(300,300)')

    xr1 = np.linspace(0,800)
    yr1 = f1(xr1)
    plt.plot(xr1,yr1,label='y <= 750-x/1.5')

    xr2 = np.linspace(40,800)
    yr2 = f2(xr2)
    plt.plot(xr2,yr2,label='y <= 750 - 1.5x')
    
    plt.legend()
    plt.show()

if __name__ == '__main__':
    config()
    maximizar_ejemplo()