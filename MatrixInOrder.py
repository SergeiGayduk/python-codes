import numpy as np
import sys

def read_file(file_name):
    file = open(file_name, "r")

    matrix = [] # here we'll put your numbers
    i = 0 # counter for matrix rows

    with file as f:
        Xs, Ys, Xf, Yf = [int(x) for x in next(f).split()]
        t = file.readline().split() # Starting points (Xs, Ys) and finishing points (Xf, Yf)
        number_of_obstacles = int(t[0])# Total of obstacles in the path

        for line in f:
            list_of_items = line.split(' ') # presumed numbers in string are divided with spaces - splittin line into list of separate strings
            if len(list_of_items) < 5:  #we will not take rows smaller then 5 into matrix
                continue

            matrix.append([]) #adding row to matrix

            for an_item in list_of_items:
                matrix[i].append(float(an_item)) #converting strings and adding floats to a row
            i += 1

        obstacles_in_order = np.reshape(matrix,(number_of_obstacles, 6))
        print(obstacles_in_order)   
            
            

input_file = "c:/Users/Lei/Documents/Python/reply/@2017/input_1.txt"
read_file(input_file)


        

        

        