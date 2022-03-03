class SatSeedDiversificationOptionSelector:
    def __init__(self):
        self.rand = None

    def set_rand(self, rand):
        self.rand = rand

    def create_arguments(self, num_dafny_calls):
        args = []
        for i in range(num_dafny_calls):
            args.append([self.make_seed_option()])
        return args

    def make_seed_option(self):
        return "/proverOpt:O:sat.random_seed={}".format(self.make_random_seed())

    def make_random_seed(self):
        return self.rand.randint(0, 2 ** 32)
