# Decision-Dependent Facility Location
## Stochastic Optimization Mini Project (NITK)

### Overview

This project implements and extends a recent research paper on facility location problems with decision-dependent uncertainty. Unlike classical stochastic facility location models where uncertainty is exogenous, here the probability distribution of demand depends on facility placement decisions themselves.

The project is being developed end-to-end, starting from deterministic models and progressively moving toward the full decision-dependent L-shaped decomposition algorithm proposed in the paper.

### Base Paper

Pantuso, G. (2025)
Solution of stochastic facility location problems with combinatorially many decision-dependent distributions
Journal of Combinatorial Optimization

## Current Status ✅
### Phase 0 — Environment & Tooling (Completed)
    Python virtual environment set up
    Gurobi (Academic License) configured and verified
    Project folder structure finalized
    Reproducible setup confirmed

### Phase 1 — Deterministic Facility Location (Completed)
    Implemented capacitated facility location model
    Binary facility decisions + continuous flows
    Verified correctness on toy instances
    Established baseline objective and constraints

### Phase 2 — Two-Stage Stochastic Facility Location (Completed)
    Introduced scenario-based stochastic demand
    Implemented expected-value objective
    Shared first-stage decisions across scenarios
    Validated solver behavior with increasing scenarios

### Phase 3 — Decision-Dependent Uncertainty (Completed, Monolithic Form)

    Introduced zones and zone-activation variables
    Implemented decision-dependent demand distributions
    Modeled distribution selection explicitly
    Identified and fixed unboundedness issues due to bilinear terms
    Enforced correct Big-M gating of flows

    Validated that:
        exactly one distribution is active
        zones activate only if facilities open
        demand responds to decisions

    ⚠️ Important Insight
    The monolithic formulation is correct but not scalable, confirming the paper’s motivation for decomposition.

    Why Phase 3 Matters (Research Insight)

    During Phase 3, the monolithic MILP:
        became quadratic and unbounded without careful gating
        required explicit enforcement of distribution activation
        demonstrated why direct enumeration of distributions is impractical
        This validates the necessity of the decision-dependent L-shaped method, not just its usefulness.

## Current Architecture
```yaml
src/
├── models/
│   ├── deterministic_facility_location.py
│   ├── stochastic_facility_location.py
│   └── decision_dependent_model.py   # monolithic (Phase 3)
│
├── utils/
│   ├── instance_generator.py
│   └── decision_dependent_instance.py
│
├── main.py
```
Next Steps 🚀 (Planned Work)
### Phase 4 — Decision-Dependent L-Shaped Decomposition
    Core contribution of the paper
    Remove explicit distribution variables (delta)
    Remove scenario explosion over all distributions

    Implement:
        Relaxed Master Problem (RMP)
        Distribution identification logic
        Distribution-specific subproblems
        Add optimality cuts derived from dual solutions
        Prove finite convergence experimentally

### Phase 5 — Experimental Evaluation
    Compare:
        monolithic vs decomposition approaches

    Study:
        scalability with number of zones
        effect of decision-dependent demand strength

    Measure:
        runtime
        number of cuts
        solution stability

### Phase 6 — Incremental Extensions (Mini-Project Contribution)
    Planned enhancements beyond the base paper:
        Zone granularity sensitivity analysis
        Alternative demand distributions (Poisson / lognormal)
        Warm-start heuristics for the master problem
        Optional risk-averse extension (CVaR)

Tools & Technologies
    Language: Python 3
    Solver: Gurobi Optimizer (Academic License)
    Optimization Type: MILP / Decomposition

Focus Areas:
    Combinatorial Optimization
    Stochastic Programming
    Decision-Dependent Uncertainty
    Academic Context

This project serves as:
    a 2-credit Mini Project (NITK)
    a research-paper-based implementation
    preparation for advanced work in:
        stochastic optimization
        decomposition methods
        operations research for ML systems

| Phase   | Description                     | Status |
| ------- | ------------------------------- | ------ |
| Phase 0 | Environment setup               | ✅      |
| Phase 1 | Deterministic FLP               | ✅      |
| Phase 2 | Stochastic FLP                  | ✅      |
| Phase 3 | Decision-dependent (monolithic) | ✅      |
| Phase 4 | L-shaped decomposition          | ⏳ Next |
| Phase 5 | Experiments                     | ⏳      |
| Phase 6 | Extensions                      | ⏳      |
