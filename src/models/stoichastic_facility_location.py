import gurobipy as gp
from gurobipy import GRB

def solve_stoichastic(I, J, S, F, C, R, d, pi, verbose=True):
    m = gp.Model("stoichastic_facility_location")
    if not verbose:
        m.setparam("OutFlag",0)
    
    #first stage variables
    x = m.addVars(I, vtype=GRB.BINARY, name="x")
    #second stage variables
    w = m.addVars(I, J, S, lb=0.0, name="w")

    #objective
    m.setObjective( -gp.quicksum(F[i]*x[i] for i in I) + gp.quicksum(pi[s]*R[i,j]*w[i, j, s] for s in S for i in I for j in J), GRB.MAXIMIZE)

    #constraints
    for s in S:
        for j in J:
            m.addConstr(gp.quicksum(w[i,j,s] for i in I) <= d[(s,j)], name=f"demand_s{s}_j{j}")
        for i in I:
            m.addConstr(gp.quicksum(w[i,j,s] for j in J) <= C[i]*x[i], name=f"capacity_s{s}_i{i}")
    
    m.optimize()

    return{
        "objective" : m.objVal,
        "x" : {i:x[i].X for i in I},
    }