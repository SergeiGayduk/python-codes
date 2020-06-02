import re # needed to use regexp to see if line in file contains only numbers

matrix = [] # here we'll put your numbers
i = 0 # counter for matrix rows

for line in open('reply/@2017/input_1.txt'): # that will iterate lines in file one by one
    if not re.match('[ 0-9\.]', line): # checking for symbols other than numbers in line
        continue # and skipping an iteration if there are any

    list_of_items = line.split(' ') # presumed numbers in string are divided with spaces - splittin line into list of separate strings
    if len(list_of_items) < 5:  #we will not take rows of 5 into matrix
        continue

    matrix.append([]) #adding row to matrix

    for an_item in list_of_items:
        matrix[i].append(float(an_item)) #converting strings and adding floats to a row
    i += 1
print(matrix)

