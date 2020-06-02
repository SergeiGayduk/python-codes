import numpy as np

def read(file_name):
    file = open(file_name, "r")
    with file as f:
        Xs, Ys, Xf, Yf = [int(x) for x in next(f).split()] # Pontos que iniciam o caminho (Xs, Ys) e Pontos que terminam o caminho (Xf, Yf)
        t = file.readline().split() # Starting points (Xs, Ys) and finishing points (Xf, Yf)
        number_of_obstacles = int(t[0])# Total of obstacles in the path

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
        #area_triangle = abs(0.5 *(((bx-ax))*(cy-ay)-((cx-ax)*(by-ay))))

        # Pythagorean theorem to find the lengths of all sides
        side1 = np.sqrt((ax - bx)**2 + (ay - by)**2) 
        side2 = np.sqrt((bx - cx)**2 + (by - cy)**2)
        side3 = np.sqrt((cx - ax)**2 + (cy - cy)**2)

        # Heron's Formula for the area of the triangle
        p = (side1 + side2 + side3)/2
        area = np.sqrt(p * (p - side1) * (p - side2) * (p - side3))
        print(side1)
        print(side2)
        print(side3)
        print(p)
        print(area)
        x = [Xs, Xf]
        y = [Ys, Yf]
     
        #return Xs, Ys, Xf, Yf, number_of_obstacles, Ax, Ay, Bx, By, Cx, Cy

file_input = "c:/Users/Lei/Documents/Python/Reply/@2017/input_1.txt"
read(file_input)