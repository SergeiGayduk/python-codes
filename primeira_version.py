import sys
import re
import numpy as np
from itertools import dropwhile

def read(file_name):
    file = open(file_name, "r")
    with file as f:
        W, H = [int(x) for x in next(f).split()] # Largura e altura do piso do escritório, respectivamente
        developers = []
        for line in f: 
            if not line.endswith(("#", '_', 'M')) and not line.startswith(('#', '_', 'M')):
                for i in f:
                    numbers_of_developers = [int(s) for s in line.split()]
                    list_of_items = line.split(' ')
                    if len(list_of_items) >= 4:
                        developers = []
                        for j in numbers_of_developers:
                            reply_company = f.readline().split()
                            developers_contributer = int(reply_company[1])
                            number_of_skills = int(reply_company[2])
                            skills = f.readlines()
                            developers.append((reply_company,  developers_contributer, number_of_skills, skills))
                    else:
                        number_of_projectManagers = (int(x) for x in file.readline().split())
                        project_managers = []
                        for k in number_of_projectManagers:
                            reply_company_manager = f.readline().split()
                            t = file.readline().split()
                            project_managers_contributers = int(t[1])

                            project_managers.append((reply_company_manager, project_managers_contributers))

        print(W)
        print(H)
        print(numbers_of_developers)
        print(developers)
        print(number_of_projectManagers)
        print(project_managers)


        
        #print(developers)
        #print(number_of_projectManagers)
        #print(project_managers)
            
input_file = "c:/Users/Lei/Documents/saves/a_solar.txt"
read(input_file)    