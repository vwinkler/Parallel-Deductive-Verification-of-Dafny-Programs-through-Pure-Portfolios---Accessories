import subprocess
from subprocess import PIPE

p1 = subprocess.Popen(["cat"], stdout=PIPE, stdin=PIPE, text=True)
p2 = subprocess.Popen(["cat"], stdout=PIPE, stdin=PIPE, text=True)
p3 = subprocess.Popen(["cat"], stdout=PIPE, stdin=PIPE, text=True)

p1.communicate(timeout=1, input="test")
p2.communicate(timeout=1, input="test")
p3.communicate(timeout=1, input="test")

print(p1.communicate())
print(p2.communicate())
print(p3.communicate())

p1.stdin.close()
p2.stdin.close()
p3.stdin.close()

p1.wait()
p2.wait()
p3.wait()
