from Process import Process
from time import time


class Z3Solver:
    def __init__(self, out, seed):
        self.start_time = None
        self.end_time = None
        self.problem = None
        self.output = None
        self.errors = None
        self.out = out
        self.seed = seed

    def run(self, problem):
        self.problem = problem
        self.start_time = time()
        self.runSolver()
        self.end_time = time()
        return self.makeResultJson()

    def runSolver(self):
        args = ["z3", "-in", "-smt2", "smt.random_seed={}".format(self.seed)]
        process = Process(args)
        stream = process.get_stream()
        stream.write_and_eof(self.problem.smt2_string)
        process.wait()
        (self.output, self.errors) = stream.read()

    def makeResultJson(self):
        result = {
            "solver_output": self.output,
            "solver_errors": self.errors,
            "total_runtime": util.format_timediff(self.start_time, self.end_time)
        }
        return result
