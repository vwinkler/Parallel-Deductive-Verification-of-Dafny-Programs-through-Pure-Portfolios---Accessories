import shlex


class CustomOptionsOptionSelector:
    def __init__(self, source):
        self.source = source

    def set_rand(self, rand):
        pass

    def create_arguments(self, num_dafny_calls):
        argument_lists = [shlex.split(line) for line in self.source]
        argument_lists = [args for args in argument_lists if len(args) == 0 or not args[0].startswith("#")]
        if len(argument_lists) != num_dafny_calls:
            raise RuntimeError((f"Stated number of calls (={num_dafny_calls}) "
                                f"and number of provided argument lists (={len(argument_lists)}) "
                                f"do not match"))
        return argument_lists
