import subprocess
from subprocess import PIPE

class SmtProcess:
    def __init__(self, args):
        self.process = subprocess.Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

    def get_pid(self):
        return self.process.pid

    def terminate(self):
        self.process.terminate()

    def get_stream(self):
        return SmtProcessStream(self.process)

    def wait(self):
        return self.process.wait()

class SmtProcessStream:
    def __init__(self, process):
        self.process = process

    def read(self):
        return self.process.communicate()

    def write(self, input):
        self.process.communicate(input, timeout=10)


    def write_eof(self):
        self.process.stdin.close()