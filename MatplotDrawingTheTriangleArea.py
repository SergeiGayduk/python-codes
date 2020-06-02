import numpy as np
import matplotlib.pyplot as plt
import math

def triangle_area(tri):
    x1, y1, x2, y2, x3, y3 = tri[0][0], tri[0][1], tri[1][0], tri[1][1], tri[2][0], tri[2][1]
    return abs(0.5 * (((x2-x1)*(y3-y1))-((x3-x1)*(y2-y1))))

def read(file_name):
    file = open(file_name, "r")
    with file as f:
        Xs, Ys, Xf, Yf = [int(x) for x in next(f).split()] # Pontos que iniciam o caminho (Xs, Ys) e Pontos que terminam o caminho (Xf, Yf)
        number_of_obstacles = [int(x) for x in next(f).split()]

        Ax, Ay = [], []
        Bx, By = [], []
        Cx, Cy = [], []
        for line in f:
            values = [int(s) for s in line.split()]
            Ax.append(values[0])
            Ay.append(values[1])
            Bx.append(values[2])
            By.append(values[3])
            Cx.append(values[4])
            Cy.append(values[5])
        # Salva o as coordenadas da primeira e segunda coluna nas variaveis ax e ay, respectivamente
        # np.array() permite realizar calculos, de forma mais simples
        ax = np.array([Ax])
        ay = np.array([Ay])

        bx = np.array([Bx])
        by = np.array([By])

        cx = np.array([Cx])
        cy = np.array([Cy])
        # Calcula a area do triângulo usando 3 vertices 
        area_triangle = abs(0.5 *(((bx-ax))*(cy-ay)-((cx-ax)*(by-ay))))

        x = [Xs, Xf]
        y = [Ys, Yf]
        # Desenha uma linha usando os pontos que iniciam o caminham e terminam o caminho
        plt.plot(x, y, linewidth=3)
        #plt.scatter(ax, ay)
        #plt.scatter(bx, by)
        #plt.scatter(cx, cy)
        plt.show()
        print(area_triangle)
        #return Xs, Ys, Xf, Yf, number_of_obstacles, Ax, Ay, Bx, By, Cx, Cy

file_input = "c:/Users/Lei/Documents/Python/Reply/@2017/input_1.txt"
read(file_input)
    