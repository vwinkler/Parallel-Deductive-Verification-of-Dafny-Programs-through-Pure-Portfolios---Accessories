import unittest
from dafnyportfolio.src.ProcessCollection import *


class ProcessCollectionAwaitTerminationTest(unittest.TestCase):

    def setUp(self):
        self.processes = ProcessCollection()
        self.p1 = self.processes.start_process(["sleep", "infinity"])

    def tearDown(self):
        self.p1.kill()
        self.p1.wait()

    def test_count_running_processes_before_kill(self):
        self.assertEqual(1, self.processes.count_running_processes())

    def test_is_running_before_kill(self):
        self.assertTrue(self.p1.is_running())

    def test_count_running_processes_after_kill(self):
        self.p1.kill()
        self.p1.wait()
        self.assertEqual(0, self.processes.count_running_processes())

    def test_is_running_after_kill(self):
        self.p1.kill()
        self.p1.wait()
        self.assertFalse(self.p1.is_running())


if __name__ == '__main__':
    unittest.main()
