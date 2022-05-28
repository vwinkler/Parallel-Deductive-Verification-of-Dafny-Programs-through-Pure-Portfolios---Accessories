import sys
import argparse
from time import time
from multiprocessing import cpu_count
from Portfolio import *
from diversification import *
import util

default_option_selector = "no-diversification"
option_selectors = {
    default_option_selector: NoDiversificationOptionSelector(),
    "seed-diversification": SeedDiversificationOptionSelector(),
    "sat-seed-diversification": SatSeedDiversificationOptionSelector(),
    "smt-seed-diversification": SmtSeedDiversificationOptionSelector(),
    "split-limit-diversification": SplitLimitDiversificationOptionSelector(),
    "dynamic-split-limit-diversification": DynamicSplitLimitDiversificationOptionSelector(),
    "stdin": CustomOptionsOptionSelector(sys.stdin)
}


def determine_instance_ids(args):
    return range(args.num_instances)


def get_commit_hash():
    return args.commit_hash if args.commit_hash is not None else util.get_current_commit_hash()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the Dafny solver in a portfolio")
    parser.add_argument(metavar="DAFNYFILE", dest="dafny_file", type=str)
    parser.add_argument(metavar="PROCEDURENAME", dest="procedure_name", type=str)
    parser.add_argument(metavar="OPTIONSELECTOR", dest="option_selector_name", choices=option_selectors.keys(),
                        default=default_option_selector)
    parser.add_argument(metavar="RESULTSFILE", dest="results_filename", type=str)
    parser.add_argument("--seed", dest="seed", type=str, default="")
    parser.add_argument("--num-instances", dest="num_instances", type=int, default=cpu_count())
    parser.add_argument("--dafny-cmd", dest="dafny_command", type=str, default="dafny")
    parser.add_argument("--commit-hash", dest="commit_hash", type=str)
    parser.add_argument("--timeout", dest="timeout", type=int, default=2 ** 31 - 1)
    args = parser.parse_args()

    chosen_option_selector = option_selectors[args.option_selector_name]
    chosen_option_selector.set_rand(Random(args.seed))
    instances = determine_instance_ids(args)
    portfolio = Portfolio(args.dafny_file, args.procedure_name, args.num_instances, instances, chosen_option_selector,
                          args.dafny_command, args.timeout)

    start_time = time()
    instances_results = portfolio.run()
    end_time = time()
    portfolio_results = {"args": vars(args),
                         "commit_hash": get_commit_hash(),
                         "total_runtime": util.format_timediff(start_time, end_time),
                         "termination_reason": portfolio.termination_reason,
                         "instances": instances_results}

    json.dump(portfolio_results, open(args.results_filename, "w"), indent=4, default=str)
