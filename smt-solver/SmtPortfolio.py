import random
from time import time

import util

class SmtPortfolio:
    def __init__(self, problem):
        self.problem = problem
        self.instances = []
        self.creation_time = time()
        self.first_solution_time = None

    def make_instances(self, num_instances):
        instances = [Z3Instance(self.problem.smt2_string, self) for i in range(num_instances)]
        for instance in instances:
            instance.seed = random.randint(0, 2 ** 32)
        self.instances.extend(instances)
        return instances

    def get_result(self):
        return {
            "instances": [instance.get_result() for instance in self.instances],
            "time_to_solution": util.format_timediff(self.creation_time, self.first_solution_time)
        }


class Z3Instance:
    def __init__(self, smt2_string, portfolio):
        self.portfolio = portfolio
        self.stream = None
        self.seed = 1337
        self.smt2_string = smt2_string
        self.termination_pending = False
        self.process_creation_time = time()
        self.solving_begin_time = None
        self.solving_end_time = None

    def get_cli_command(self):
        return ["z3", "-in", "-smt2", "smt.random_seed={}".format(self.seed)]

    def assign_process(self, stream):
        self.solving_begin_time = time()
        self.stream = stream
        stream.write_and_eof(self.smt2_string)

    def unassign_process(self):
        (self.output, self.errors) = self.stream.read()
        self.stream = None
        self.solving_end_time = time()

        if self.output in ["unsat\n", "sat\n"]:
            self.portfolio.first_solution_time = time()
            for instance in self.portfolio.instances:
                instance.termination_pending = True


    def has_termination_pending(self):
        return self.termination_pending

    def get_result(self):
        return {
            "solver_output": self.output,
            "solver_errors": self.errors,
            "wall_clock_working_time": util.format_timediff(self.solving_begin_time, self.solving_end_time),
            "wall_clock_total_time": util.format_timediff(self.process_creation_time, self.solving_end_time)
        }
