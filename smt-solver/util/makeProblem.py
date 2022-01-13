import json
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a portfolio of SMT-Solvers")
    parser.add_argument("--in", dest="in_filename")
    parser.add_argument("--out", dest="out_filename")
    
    args = parser.parse_args()
    
    problem = {}
    with open(args.in_filename, "r") as file:
        problem["smt2"] = file.read()
        
    with open(args.out_filename, "w") as file:
        json.dump(problem, file)
