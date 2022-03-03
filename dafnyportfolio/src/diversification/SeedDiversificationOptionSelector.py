from random import Random


class SeedDiversificationOptionSelector:
    def __init__(self):
        self.rand = None

    def set_rand(self, rand):
        self.rand = rand

    def create_arguments(self, num_dafny_calls):
        args = []
        for i in range(num_dafny_calls):
            args.append(self.make_seed_options())
        return args

    def make_seed_options(self):
        rand = Random(self.make_random_seed(self.rand))
        option_prefixes = ["sat", "smt", "fp.spacer", "sls"]
        options = ["/proverOpt:O:{}.random_seed={}".format(p, self.make_random_seed(rand)) for p in option_prefixes]
        return options

    def make_random_seed(self, rand):
        return rand.randint(0, 2 ** 32)
