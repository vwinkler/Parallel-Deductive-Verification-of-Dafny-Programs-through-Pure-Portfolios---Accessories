import unittest
from dafnyportfolio.src.ProcessCollection import *


class ProcessCollectionAwaitTerminationTest(unittest.TestCase):

    def setUp(self):
        self.processes = ProcessCollection()
        self.p1 = self.processes.start_process(["sleep", "0.2s"])
        self.p2 = self.processes.start_process(["sleep", "0.4s"])

    def tearDown(self):
        self.p1.wait()
        self.p2.wait()

    def test_await_first_termination(self):
        self.assertIn(self.processes.await_termination_of_any_process(), [self.p1, self.p2])

    def test_await_second_termination(self):
        terminated_process = self.processes.await_termination_of_any_process()
        remaining_processes = [p for p in [self.p1, self.p2] if p is not terminated_process]
        self.assertIn(self.processes.await_termination_of_any_process(), remaining_processes)

    def test_count_start(self):
        self.assertLessEqual(self.processes.count_running_processes(), 2)

    def test_count_first_termination(self):
        self.processes.await_termination_of_any_process()
        self.assertLessEqual(self.processes.count_running_processes(), 1)

    def test_count_second_termination(self):
        self.processes.await_termination_of_any_process()
        self.processes.await_termination_of_any_process()
        self.assertLessEqual(self.processes.count_running_processes(), 0)


if __name__ == '__main__':
    unittest.main()
