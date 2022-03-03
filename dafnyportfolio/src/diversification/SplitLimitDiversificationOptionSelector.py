class SplitLimitDiversificationOptionSelector:
    def set_rand(self, rand):
        pass

    def create_arguments(self, num_dafny_calls):
        args = []

        args.append([self.make_max_keep_going_splits_arg(2)])

        for i in range(num_dafny_calls - len(args)):
            args.append([self.make_max_num_splits_arg(2 ** i)])
        return args

    def make_max_keep_going_splits_arg(self, num):
        return "/vcsMaxKeepGoingSplits:{}".format(num)

    def make_max_num_splits_arg(self, num):
        return "/vcsMaxSplits:{}".format(num)
