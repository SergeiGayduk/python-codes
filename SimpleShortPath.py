# If the list is not too big, the easiest solution I find is using the where function of the numpy library 
# to find the cells which have the value you are looking for. So, you will need to convert your list into 
# a numpy array.
# The code below might be simplified to make it shorter and more efficient, 
# but in this way it will be clearer. By the way, you can compute two kind of distances: 
# the typical euclidean and the manhattan.
# If there is more than one target cell at the same distance of the origin cell, min_coords corresponds to 
# the first cell found (first by rows, then by columns).

import numpy as np

# The list needs to be transformed into an array in order to use the np.where method
# arr = np.random.randint(5, size=(6, 6))
arr = np.array([[0, 0, 0, 1, 1, 3],
                [0, 0, 2, 1, 1, 0],
                [0, 0, 1, 1, 1, 1],
                [3, 0, 3, 1, 1, 1], ])

# Origin cell to make the search
x0, y0 = (1, 1)
targetValue = 3

# This is the keypoint of the problem: find the positions of the cells containing the searched value
positions = np.where(arr == targetValue)
x, y = positions

dx = abs(x0 - x)  # Horizontal distance
dy = abs(y0 - y)  # Vertical distance

# There are different criteria to compute distances
euclidean_distance = np.sqrt(dx ** 2 + dy ** 2)
manhattan_distance = abs(dx + dy)
my_distance = euclidean_distance  # Criterion choice
min_dist = min(my_distance)
print(min_dist)

min_pos = np.argmin(my_distance)  # This method will only return the first occurrence (!)
min_coords = x[min_pos], y[min_pos]
print(min_coords)