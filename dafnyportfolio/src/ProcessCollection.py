import os
import signal
from subprocess import Popen, PIPE

any_cpu = None


class CpuQueueBwUniClusterSinglePartition:
    def __init__(self):
        self.queue = self.get_preferred_cpu_order()

    def get_preferred_cpu_order(self):
        first_hyperthreads = [cpu for k in range(0, 9) for cpu in list(range(0 + k, 31 + k, 10))]
        second_hyperthreads = [cpu for k in range(0, 9) for cpu in list(range(40 + k, 71 + k, 10))]
        return first_hyperthreads + second_hyperthreads

    def pop(self):
        try:
            return self.queue.pop(0)
        except IndexError:
            raise RuntimeError("No CPU left for this process")

    def add(self, cpu):
        self.queue.append(cpu)


class ProcessCollection:
    def __init__(self, cpu_pool=None):
        self.processesMarkedTerminated = set()
        self.processes = dict()
        self.cpu_pool = cpu_pool

    def start_process(self, args, stdin=PIPE, stdout=PIPE, stderr=PIPE):
        cpu = self._get_cpu_from_pool()
        process = Process(args, cpu, stdin=stdin, stdout=stdout, stderr=stderr)
        self.processes[process.get_pid()] = process
        return process

    def _get_cpu_from_pool(self):
        if not self._cpu_assignment_is_enabled():
            return any_cpu
        return self.cpu_pool.pop()

    def kill_all(self):
        for process in self.processes.values():
            process.kill()

    def await_termination_of_all_processes(self):
        while self.count_running_processes() > 0:
            self.await_termination_of_any_process(timeout=2 ** 31 - 1)

    def count_running_processes(self):
        return len(self.find_running_processes())

    def find_running_processes(self):
        return set.difference(self.get_all_processes(), self.find_terminated_processes())

    def get_all_processes(self):
        return set(self.processes.values())

    def find_terminated_processes(self):
        return {p for p in self.get_all_processes() if not p.is_running()}

    def await_termination_of_any_process(self, timeout=2 ** 31 - 1):
        self._raise_if_empty()
        process = self._try_await_next_termination(timeout)
        self._clean_up_after_terminated_process(process)
        self.processesMarkedTerminated.add(process)
        return process

    def _raise_if_empty(self):
        if self.get_all_processes() == self.processesMarkedTerminated:
            raise RuntimeError("All processes have terminated.")

    def _try_await_next_termination(self, timeout):
        try:
            process = self._await_next_termination_with_timelimit(timeout)
        except ChildProcessError:
            process = self._select_any_unmarked_terminated_process()
        return process

    def _await_next_termination_with_timelimit(self, timeout):
        self._set_timeout(timeout)
        terminated_pid = self._await_next_termination()
        self._unset_timeout()
        return terminated_pid

    def _unset_timeout(self):
        signal.alarm(0)

    def _set_timeout(self, timeout):
        def handle_timeout(signum, frame):
            raise TimeoutError()

        signal.signal(signal.SIGALRM, handle_timeout)
        signal.alarm(timeout)

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

    def _clean_up_after_terminated_process(self, process):
        cpu = process.get_assigned_cpu()
        self.return_cpu_to_pool(cpu)

    def return_cpu_to_pool(self, cpu):
        if cpu == any_cpu and self._cpu_assignment_is_enabled():
            self.cpu_pool.add(cpu)

    def _cpu_assignment_is_enabled(self):
        return self.cpu_pool is not None


class Process:
    def __init__(self, args, cpu=any_cpu, stdin=PIPE, stdout=PIPE, stderr=PIPE):
        self.stdin_is_pipe = stdin == PIPE
        self.stdout_is_pipe = stdout == PIPE
        self.stderr_is_pipe = stderr == PIPE
        self.wrapped_process = Popen(args, stdin=stdin, stdout=stdout, stderr=stderr, text=True)
        self.assigned_cpu = cpu
        self._establish_cpu_assignment()

    def _establish_cpu_assignment(self):
        if self.assigned_cpu is not any_cpu:
            print(self.assigned_cpu)
            os.sched_setaffinity(self.wrapped_process.pid, [self.assigned_cpu])

    def __del__(self):
        try:
            if self.stdin_is_pipe:
                self.wrapped_process.stdin.close()
            if self.stdout_is_pipe:
                self.wrapped_process.stdout.close()
            if self.stderr_is_pipe:
                self.wrapped_process.stderr.close()
        except AttributeError:
            pass

    def get_pid(self):
        return self.wrapped_process.pid

    def get_assigned_cpu(self):
        return self.assigned_cpu

    def is_running(self):
        return self.wrapped_process.poll() is None

    def kill(self):
        self.wrapped_process.kill()

    def wait(self):
        self.wrapped_process.wait()
