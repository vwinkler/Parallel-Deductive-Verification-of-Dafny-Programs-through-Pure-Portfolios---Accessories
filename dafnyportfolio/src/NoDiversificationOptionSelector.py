class NoDiversificationOptionSelector:
    def create_arguments(self, num_dafny_calls):
        return [[] for _ in range(num_dafny_calls)]
