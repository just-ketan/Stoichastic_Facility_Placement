import numpy as np

def generate_toy_instance():
    # very small deterministic instance
    I = [0,1,2] # facilities
    J = [0,1,2,3]   # customers

    F = {0:30, 1:25, 2:20}  #opening cost
    C = {0:40, 1:35, 2:30}  #capacities
    d = {0:15, 1:20, 2:10, 3:25}    #demands

    R = {}
    for i in I:
        for j in J:
            R[(i,j)] = 10 - abs(i-j)    # simple revenue pattern
    
    return I, J, F, C, d, R