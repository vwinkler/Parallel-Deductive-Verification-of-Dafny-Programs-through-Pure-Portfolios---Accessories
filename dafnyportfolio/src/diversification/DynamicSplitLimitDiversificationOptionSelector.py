class DynamicSplitLimitDiversificationOptionSelector:
    def set_rand(self, rand):
        pass

    def create_arguments(self, num_dafny_calls):
        return [[self.make_max_keep_going_splits_arg(2 ** i)] for i in range(num_dafny_calls)]

    def make_max_keep_going_splits_arg(self, num):
        return "/vcsMaxKeepGoingSplits:{}".format(num)
