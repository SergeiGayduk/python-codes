import sys
from operator import itemgetter
import numpy as np


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
        
        return Xs, Ys, Xf, Yf, number_of_obstacles, ax, ay, bx, by, cx, cy

def write(file_name, solution):
    file = open(file_name, "w")
    string_solution = []
    for coordinates_points in solution:
        string_solution.append(" ".join((str(x) for x in coordinates_points)))
    file.write("\n".join(string_solution))


def shortestpath(graph,start,end,visited=[],distances={},predecessors={}):
    """Find the shortest path between start and end nodes in a graph"""
    # we've found our end node, now find the path to it, and return
    i = 0
    while np.all(graph[i] >= 0):
        if start==end:
            path=[]
            while end != None:
                path.append(end)
                end=predecessors.get(end,None)
                return distances[start], path[::-1]
            # detect if it's the first time through, set current distance to zero
            if not visited: distances[start]=0
            # process neighbors as per algorithm, keep track of predecessors
            for neighbor in graph[start]:
                if neighbor not in visited:
                    neighbordist = distances.get(neighbor,sys.maxsize)
                    tentativedist = distances[start] + graph[start][neighbor]
                if tentativedist < neighbordist:
                    distances[neighbor] = tentativedist
                    predecessors[neighbor]=start
                    # neighbors processed, now mark the current node as visited
                    visited.append(start)
                    # finds the closest unvisited node to the start
                    unvisiteds = dict((k, distances.get(k,sys.maxsize)) for k in graph if k not in visited)
                    closestnode = min(unvisiteds, key=unvisiteds.get)
                # now we can take the closest node and recurse, making it current
                return shortestpath(graph,closestnode,end,visited,distances,predecessors)
    

def main():
    file_name = "c:/Users/Lei/Documents/Python/reply/@2017/input_1.txt"
    Xs, Ys, Xf, Yf, number_of_obstacles, ax, ay, bx, by, cx, cy = read(file_name)
    '''
    Testando as variaveis

    print("Starting Points:")
    print(Xs, Ys)
    print("Finishing Points:")
    print(Xf, Yf)
    print("Number of obstacles:")
    print(number_of_obstacles)
    print("Ax:")
    print(ax)
    print("Ay:")
    print(ay)
    print("Bx:")
    print(bx)
    print("By:")
    print(by)
    print("Cx:")
    print(cx)
    print("Cy:")
    print(cy)

    '''
    # Como no dijkstra não pode ter dois valores de inicio / fim
    # Se o começo for igual a 0 ou o menor valor, então considerarei o menor valor
    if Xs or Ys == 0:
        starting_point = 0
    elif Xs < Ys:
        starting_point = Xs
    elif Ys < Xs:
        starting_point = Ys
    # Se ambas as variaveis do fim do caminho forem iguais e se algum valor for maior que o outro 
    # será usado o valor mais alto 
    if Xf == Yf:
        finishing_point = Xf
    elif Xf > Yf:
        finishing_point = Xf
    elif Xf < Yf:
        finishing_point = Yf
    # abs(0.5 * (((x2-x1)*(y3-y1))-((x3-x1)*(y2-y1)))) 
    # triangle.py
    triangle = abs(1 * (((bx-ax)*(cy-ay))-((cx-ax)*(by-ay))))

    print(shortestpath(triangle, starting_point, finishing_point))


if __name__ == "__main__":
    main() 