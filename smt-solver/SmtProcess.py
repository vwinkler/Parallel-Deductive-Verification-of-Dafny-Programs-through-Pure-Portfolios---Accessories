import subprocess
from subprocess import PIPE
import threading
from time import time


class SmtProcess:
    def __init__(self, args):
        self.process = subprocess.Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)
        self.stream = SmtProcessStream(self.process)

    def get_pid(self):
        return self.process.pid

    def terminate(self):
        self.process.terminate()

    def get_stream(self):
        return self.stream

    def wait(self):
        return self.process.wait()

    def has_terminated(self):
        return self.process.poll() is not None


class SmtProcessStream:
    def __init__(self, process):
        self.thread = None
        self.process = process
        self.lock = threading.Lock()

    def read(self):
        self.lock.acquire()
        try:
            return self.process.communicate()
        except Exception as e:
            raise e
        finally:
            self.lock.release()

    def write_and_eof(self, input):
        self.thread = threading.Thread(target=self.write_and_eof_blocking, args=(input,))
        self.thread.start()

    def write_and_eof_blocking(self, input):
        self.lock.acquire()
        try:
            self.process.communicate(input)
            self.process.stdin.close()
        except Exception as e:
            raise e
        finally:
            self.lock.release()

    def write_eof(self):
        self.lock.acquire()
        try:
            self.process.stdin.close()
        except Exception as e:
            raise e
        finally:
            self.lock.release()
