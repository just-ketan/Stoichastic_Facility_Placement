import gurobipy as gp
from gurobipy import GRB

def solve_decision_dependent(I, J, Z, I_z, D, F, C, R, scenarios, pi, verbose=True):
    m = gp.Model("decision_dependent")
    if not verbose:
        m.setParam("OutputFlag",0)

    #variable
    x = m.addVars(I, vtype=GRB.BINARY, name="x")
    y = m.addVars(Z, vtype=GRB.BINARY, name="y")
    delta = m.addVars(D.keys(), vtype=GRB.BINARY, name="delta")
    w = m.addVars([(i, j, d, s) for i in I for j in J for d in D for s in pi], lb=0.0, name="w")

    #objective
    m.setObjective( -gp.quicksum(F[i]*x[i] for i in I) + gp.quicksum( pi[s] * R[i, j] * w[i, j, d, s] for i in I for j in J for d in D for s in pi) )

    # zone activation constraints
    for z in Z:
        m.addConstr(gp.quicksum(x[i] for i in I_z[z]) >= y[z], name=f"zone_lb_{z}")
        m.addConstr(gp.quicksum(x[i] for i in I_z[z]) <= len(I_z[z])*y[z], name=f"zone_lb_{z}")

    # distribution selection
    m.addConstr(gp.quicksum(delta[d] for d in D) == 1)
    for d,(y0, y1) in D.items():
        m.addConstr(y[0] == y0*delta[d] + y[0]*(1-delta[d]))
        m.addConstr(y[1] == y1*delta[d] + y[1]*(1-delta[d]))

    #capacity and demand
    for d, (y0, y1) in D.items():
        m.addConstr(y[0] >= y0 * delta[d])
        m.addConstr(y[0] <= y0 + (1 - delta[d]))
        m.addConstr(y[1] >= y1 * delta[d])
        m.addConstr(y[1] <= y1 + (1 - delta[d]))


    m.optimize()

    return{
        "objective" : m.objVal,
        "x" : {i:x[i].X for i in I},
        "y" : {z:y[z].X for z in Z},
        "delta" : {d:delta[d].X for d in D},
    }