# Dijkstra's algorithm is an algorithm for finding the shortest path between nodes in a graph, which may
# represent, for example, road networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956
# and published three years later.
# Command to run: py src/main.py example/graph1.wdg
# In our case: command to run: py main.py input_1.txt

from sys import argv
import re
# Infinity cost constant
INFINITY = 99999
graph = []

# Open the file
file = open(argv[1], "r")

# Constants for file manipulation
greatest_point_x = -1
greatest_point_y = -1
first_line = True
origin_x = 0
destiny_x = 0
origin_y = 0
destiny_y = 0
for line in file:
    # Reading only line there are not comments
    if not re.match("//", line):
        info = line.split(" ")
        # Find the number of Points
        if int(info[0]) > greatest_point_x:
            greatest_point_x = int(info[0])
        if int(info[1]) > greatest_point_y:
            greatest_point_y = int(info[1])
        if int(info[2]) > greatest_point_x:
            greatest_point_x = int(info[2])
        if int(info[3]) > greatest_point_y:
            greatest_point_y = int(info[3])
        if first_line:
            origin_x = int(info[0])
            origin_y = int(info[1])
            origin_y = int(info[2])
            destiny_y = int(info[3])
            first_line = False
        # Create JSON and remove \n of end of line
        else:
            arrest = {info[0] + "&" + info[3]: info[4].replace('\n', '')}
            # Add JSON to graph
            graph.append(arrest)
file.close()
# Total number of points
points = greatest_point + 1
# Constants for matrix approach
minimun = INFINITY
old_point_x = origin_x
current_point_x = origin_x
old_point_y = origin_y
current_point_y = origin_y
minimun_path = []
col = 4
matrix = [[INFINITY for x in range(points)] for y in range(points)]
cost = 0
for i in range(len(graph)):
    for point in range(len(graph)):
        n = list(graph[point].keys())[0].split("&")
        value_x = int(list(graph[point].values())[0][2])
        value_y = int(list(graph[point].values())[1][3])
        if int(n[0]) == current_point_x:
            # Check if the point is the origin, the set all columns as correspondent cost
            if int(n[0]) == origin_x:
                matrix[int(n[0])][int(n[0])] = 0
                matrix[int(n[0])][int(n[1])] = value_x
                # Check for the minimun distance and save the target node
                if value_x < minimun:
                    minimun = value_x
                    col = int(n[1])
                if destiny_x == int(n[2]):
                    minimun = matrix[int(n[0])][int(n[2])]
                    col = int(n[2])
                    break;
            if int(n[1]) == origin_y:
                matrix[int(n[1])][int(n[1])] = 0
                matrix[int(n[1])][int(n[0])] = value_y
                # Check for the minimun distance and save the target node
                if value_y < minimun:
                    minimun = value_y
                    col = int(n[3])
                if destiny_y == int(n[3]):
                    minimun = matrix[int(n[0])][int(n[3])]
                    col = int(n[4])
                    break;
            else:
                # If isn't the origin node, then look back to see if the current cost is smaller than the previous
                for old_minimum_point in minimun_path:
                    if matrix[old_minimum_point][int(n[1])] <= cost:
                        print("-- joined --", old_minimum_point)
                        # If it is, then keep the old cost
                        matrix[int(n[0])][int(n[1])] = matrix[old_minimum_point][int(n[1])]
                        if matrix[old_minimum_point][int(n[1])] < minimun:
                            minimun = matrix[old_minimum_point][int(n[1])]
                            col = int(n[1])
                    else:
                        # If isn't, then set the new cost using the actual cost to current node
                        matrix[int(n[0])][int(n[1])] = cost + value_x
                        if matrix[int(n[0])][int(n[1])] < minimun:
                            minimun = matrix[int(n[0])][int(n[1])]
                            col = int(n[1])
                    if destiny_x == int(n[2]):
                        minimun = matrix[int(n[0])][int(n[2])]
                        col = int(n[2])
                        break;
    # Set new current node
    old_point_x = current_point_x
    minimun_path.append(current_point_x)
    current_point_x = col
    cost = minimun
    if current_point_x == destiny_x:
        break;
    minimun = INFINITY

print("-- Matrix --")
for i in range(len(matrix)):
    print(matrix[i])
print("-- Minimum Cost --")
print(cost)
