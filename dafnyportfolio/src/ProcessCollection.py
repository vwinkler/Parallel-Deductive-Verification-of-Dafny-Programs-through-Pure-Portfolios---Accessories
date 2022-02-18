import os
from subprocess import Popen, PIPE


class ProcessCollection:
    def __init__(self):
        self.processesMarkedTerminated = set()
        self.processes = dict()

    def start_process(self, args):
        process = Process(args)
        self.processes[process.get_pid()] = process
        return process

    def count_running_processes(self):
        return len(self.find_running_processes())

    def find_running_processes(self):
        return set.difference(self.get_all_processes(), self.find_terminated_processes())

    def get_all_processes(self):
        return set(self.processes.values())

    def find_terminated_processes(self):
        return {p for p in self.get_all_processes() if not p.is_running()}

    def await_termination_of_any_process(self):
        self._raise_if_empty()
        process = self._try_await_next_termination()
        self.processesMarkedTerminated.add(process)
        return process

    def _raise_if_empty(self):
        if self.get_all_processes() == self.processesMarkedTerminated:
            raise RuntimeError("All processes have terminated.")

    def _try_await_next_termination(self):
        try:
            process = self._await_next_termination()
        except ChildProcessError:
            process = self._select_any_unmarked_terminated_process()
        return process

    def _await_next_termination(self):
        pid = -1
        while not self._has_pid(pid):
            pid, _ = os.wait()
        return self.processes[pid]

    def _has_pid(self, pid):
        return (pid in self.processes) and (pid not in self.processesMarkedTerminated)

    def _select_any_unmarked_terminated_process(self):
        return next(iter(self._find_unmarked_terminated_processes()))

    def _find_unmarked_terminated_processes(self):
        return set.difference(self.find_terminated_processes(), self.processesMarkedTerminated)


class Process:
    def __init__(self, args):
        self.wrapped_process = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

    def __del__(self):
        self.wrapped_process.stdin.close()
        self.wrapped_process.stdout.close()
        self.wrapped_process.stderr.close()

    def get_pid(self):
        return self.wrapped_process.pid

    def is_running(self):
        return self.wrapped_process.poll() is None

    def kill(self):
        self.wrapped_process.kill()

    def wait(self):
        self.wrapped_process.wait()
