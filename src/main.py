from utils.instance_generator import generate_stoichastic_instance
from models.stoichastic_facility_location import solve_stoichastic

def main():
    I, J, S, F, C, R, d, pi = generate_stoichastic_instance(num_scenarios=5)
    sol = solve_stoichastic(I, J, S, F, C, R, d, pi)
    print("\n Objective Values: ", sol["objective"])
    print("\n Open facilities: ")
    for i, val in sol["x"].items():
        print(f" facility{i}: {int(round(val))}")
    # print("\n Non-zero flows:")
    # for (i,j), val in sol["w"].items():
    #     if val > 1e-6:
    #         print(f" w[{i},{j}] = {val:.2f}")

if __name__ == "__main__":
    main()