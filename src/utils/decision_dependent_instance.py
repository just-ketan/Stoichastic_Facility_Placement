import numpy as np

def generate_decision_dependent_instance(num_scenarios=3, seed=1):
    np.random.seed(seed)

    I = [0,1,2]
    J = [0,1,2]
    Z = [0,1]   # zones

    I_z = {
        0 : [0,1],  # zone 0
        1 : [2],    # zone 1
    }

    # cost and capacity
    F = {0:20, 1:22, 2:18}
    C = {0:30, 1:20, 2:25}
    R = {(i,j):10 for i in I for j in J}

    base_demand = {0:10, 1:12, 2:8}

    # all possible distributions
    D = {
        0:(0,0),
        1:(1,0),
        2:(0,1),
        3:(1,1),
    }

    # scenarios
    scenarios = {}
    for d, (y0, y1) in D.items():
        scenarios[d] = {}
        for s in range(num_scenarios):
            scenarios[d][s] = {}
            for j in J:
                mu = base_demand[j]
                if y0 == 1:
                    mu += 5
                if y1 == 1:
                    mu += 8
                scenarios[d][s][j] = max(0, int(np.random.normal(mu,2)))
    
    pi = {s:1.0/num_scenarios for s in range(num_scenarios)}

    return I, J, Z, I_z, D, F, C, R, scenarios, pi