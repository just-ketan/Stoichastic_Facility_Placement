from utils.instance_generator import generate_toy_instance
from models.deterministic_facility_location import solve_deterministic

def main():
    I, J, F, C, d, R = generate_toy_instance()
    sol = solve_deterministic(I, J, F, C, d, R)
    print("\n Objective Values: ", sol["objective"])
    print("\n Open facilities: ")
    for i, val in sol["x"].items():
        print(f" facility{i}: (int(round(val)))")
    print("\n Non-zero flows:")
    for (i,j), val in sol["w"].items():
        if val > 1e-6:
            print(f" w[{i},{j}] = {val:.2f}")

if __name__ == "__main__":
    main()