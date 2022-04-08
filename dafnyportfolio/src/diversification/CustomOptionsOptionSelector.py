import shlex


class CustomOptionsOptionSelector:
    def __init__(self, source):
        self.source = source

    def set_rand(self, rand):
        pass

    def create_arguments(self, num_dafny_calls):
        argument_lists = [shlex.split(line) for line in self.source]
        argument_lists = [args for args in argument_lists if len(args) > 0]
        if len(argument_lists) != num_dafny_calls:
            raise RuntimeError("Stated number of calls and number of provided argument lists do not match")
        return argument_lists
