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


class NoCpuQueue:
    def pop(self):
        return any_cpu

    def add(self, _):
        pass
