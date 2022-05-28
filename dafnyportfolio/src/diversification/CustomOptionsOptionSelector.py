import shlex


class CustomOptionsOptionSelector:
    def __init__(self, source):
        self.source = source

    def set_rand(self, rand):
        pass

    def create_arguments(self, _):
        argument_lists = [shlex.split(line) for line in self.source]
        argument_lists = [args for args in argument_lists if len(args) == 0 or not args[0].startswith("#")]
        return argument_lists
