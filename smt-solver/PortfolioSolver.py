import os
from random import Random
from time import sleep
from time import time

from SmtPortfolio import SmtPortfolio
from Process import Process
import util


class PortfolioSolver:
    def __init__(self, output, seed):
        self.output = output
        self.random = Random(seed)
        self.problem = None
        self.start_time = None
        self.end_time = None
        self.processes = None
        self.portfolio = None

    def run(self, problem):
        self.problem = problem
        self.start_time = time()
        self.runPortfolio()
        self.end_time = time()
        return self.makeResultJson()

    def runPortfolio(self):
        self.portfolio = SmtPortfolio(self.problem, self.random.randint(0, 2 ** 32))
        self.startProcesses()

        self.awaitTerminationOfAllProcesses()

    def startProcesses(self):
        self.processes = dict()
        instances = self.portfolio.make_instances(4)
        for instance in instances:
            self.startProcess(instance)

    def startProcess(self, instance):
        command = instance.get_cli_command()
        process = Process(command)
        pid = process.get_pid()
        self.processes[pid] = (process, instance)
        self.printStartMessage(command, pid)
        self.assignProcessToInstance(instance, process)

    def assignProcessToInstance(self, instance, process):
        instance.assign_process(process.get_stream())
        if instance.termination_pending:
            self.forceProcessTermination(process)

    def awaitTerminationOfAllProcesses(self):
        while len(self.processes) > 0:
            self.tryAwaitTerminatedProcess()
            self.cleanUpTerminatedProcesses()

    def tryAwaitTerminatedProcess(self):
        try:
            pid = self.awaitTerminatedProcess()
        except ChildProcessError:
            pid = None
        return pid

    def awaitTerminatedProcess(self):
        return self.awaitNextProcessTermination()

    def awaitNextProcessTermination(self):
        pid, _ = os.wait()
        return pid

    def awaitTerminationOfSomeProcess(self):
        pid = next(iter(self.processes.keys()))
        (process, instance) = self.processes[pid]
        process.wait()
        return pid

    def forceProcessTermination(self, process):
        process.terminate()
        self.cleanUpTerminatedProcess(process.get_pid())

    def cleanUpTerminatedProcesses(self):

        terminatedProcesses = [pid for pid, (process, _) in self.processes.items() if process.has_terminated()]
        for pid in terminatedProcesses:
            self.cleanUpTerminatedProcess(pid)

    def cleanUpTerminatedProcess(self, pid):
        (process, instance) = self.processes[pid]
        del self.processes[pid]
        instance.unassign_process()
        self.printTerminationMessage(pid)
        self.terminatePendingProcesses()

    def terminatePendingProcesses(self):
        for pid, (process, instance) in self.processes.items():
            if instance.has_termination_pending():
                process.terminate()

    def makeResultJson(self):
        result = {
            "portfolio": self.portfolio.get_result(),
            "total_runtime": util.format_timediff(self.start_time, self.end_time)
        }
        return result

    def printStartMessage(self, command, pid):
        message = "\trunning '{}' on pid={} (total: {} processes)\n".format(" ".join(command), pid, len(self.processes))
        self.output.write(message)

    def printTerminationMessage(self, pid):
        message = "\tprocess with pid={} terminated (total: {} processes remaining)\n".format(pid, len(self.processes))
        self.output.write(message)