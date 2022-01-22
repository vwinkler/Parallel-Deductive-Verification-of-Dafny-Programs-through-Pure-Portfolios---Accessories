import sys
from io import open
import subprocess
from subprocess import PIPE
import argparse
import json

from SmtProblem import SmtProblem
from solvers import make_solver, solver_names


def file_tuple(s):
    try:
        in_file, out_file = s.split(':')
        return {"in": in_file, "out": out_file}
    except:
        raise argparse.ArgumentTypeError("Problems must be FILENAME:FILENAME")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a portfolio of SMT-Solvers")
    parser.add_argument("--solver", metavar="STRING", dest="solver", type=str, choices=solver_names)
    parser.add_argument("--problems", "-f", metavar="IN_FILENAME:OUT_FILENAME", dest="filenames", type=file_tuple,
                        nargs="+")
    parser.add_argument("--seed", metavar="STRING", dest="seed", type=str)

    args = parser.parse_args()

    # simple mode:
    # Run one portfolio after the other. Each is given 4 processes. Wait for one to terminate.
    for problem_files in args.filenames:
        print("Running '{}'; writing results to '{}'...".format(problem_files["in"], problem_files["out"]))
        in_file = open(problem_files["in"], "r")
        out_file = open(problem_files["out"], "w")
        problem = SmtProblem(in_file)
        solver = make_solver(sys.stdout, args)

        result = solver.run(problem)

        json.dump(result, out_file, indent=2)
