import numpy as np

def generate_stoichastic_instance(num_scenarios=5, seed=42):
    # very small deterministic instance
    I = [0,1,2] # facilities
    J = [0,1,2,3]   # customers
    S = list(range(num_scenarios))
    F = {0:30, 1:25, 2:20}  #opening cost
    C = {0:40, 1:35, 2:30}  #capacities
    d = {0:15, 1:20, 2:10, 3:25}    #demands

    R = {(i,j): 10 - abs(i-j) for i in I for j in J}

    #base demand
    base_demand = {0:15, 1:20, 2:10, 3:25}

    #scenario demands
    d= {}
    for s in S:
        for j in J:
            d[(s,j)] = max(
                0,
                int(np.random.normal(loc=base_demand[j], scale=3))
            )
    
    #equal probability
    pi = {s:1.0/num_scenarios for s in S}

    return I, J, S, F, C, R, d, pi