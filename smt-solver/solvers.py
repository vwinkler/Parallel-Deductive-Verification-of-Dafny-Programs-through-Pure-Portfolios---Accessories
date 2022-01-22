from PortfolioSolver import PortfolioSolver
from Z3Solver import Z3Solver


def make_portfolio_solver(out, args):
    return PortfolioSolver(out, args.seed)


def make_z3_solver(out, args):
    return Z3Solver(out, args.seed)


solver_runners = {
    "portfolio": make_portfolio_solver,
    "z3": make_z3_solver
}

solver_names = solver_runners.keys()

def make_solver(out, args):
    return solver_runners[args.solver](out, args)
