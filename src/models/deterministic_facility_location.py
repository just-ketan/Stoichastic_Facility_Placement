import gurobipy as gp
from gurobipy import GRB

def solve_deterministic(I, J, F, C, d, R, verbose=True):
    m = gp.Model("deterministic_facility_location")
    if not verbose:
        m.setParam("OutputFlag",0)
    
    # variables
    x = m.addVars(I, vtype=GRB.BINARY, name="x")
    w = m.addVars(I,J,lb=0.0, name="w")

    # objective
    m.setObjective(
        gp.quicksum(R[i,j]*w[i,j] for i in I for j in J)
        - gp.quicksum(F[i]*x[i] for i in I),
        GRB.MAXIMIZE
    )

    # demand constraints
    for j in J:
        m.addConstr(gp.quicksum(w[i,j] for i in I) <= d[j], name=f"demand_(J)")

    # capcity constraint
    for i in I:
        m.addConstr(
            gp.quicksum(w[i,j] for j in J) <= C[i]*x[i],
            name = f"capacity_{i}"
        )
    
    m.optimize()

    solution={
        "objective":m.objVal,
        "x":{i:x[i].X for i in I},
        "w":{(i,j): w[i,j].X for i in I for j in J}
    }

    return solution