import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Configuración para graficar
def config():
    matplotlib.use('TkAgg')

# Definición de la inecuación
def f(x):
    return 5 - (2*x)

def punto_uno():
    #Puntos en los cuales voy a evaluar la función para poder graficar
    xr = np.linspace(-3,8)
    #Valores de x evaluados en la función
    yr = f(xr)

    #Dibujando valores en el lienzo
    plt.plot(xr,yr,label='y < 5-2x')

    #Coloreando el Aŕea solución
    plt.fill([-9,-3,8,0],[9,9,-9,-9],'g',alpha=0.75, label = 'Área solución')

    # Ajustes estéticos
    plt.legend()
    # Mostrar gráfica resultado
    plt.show()


if __name__ == '__main__':
    config()
    punto_uno()