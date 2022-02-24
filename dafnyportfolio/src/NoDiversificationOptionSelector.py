class NoDiversificationOptionSelector:
    def set_rand(self, rand):
        pass

    def create_arguments(self, num_dafny_calls):
        return [[] for _ in range(num_dafny_calls)]
