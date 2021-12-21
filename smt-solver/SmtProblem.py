import json


class SmtProblem:
    def __init__(self, file):
        problem = json.load(file)
        self.smt2_string = problem["smt2"]
