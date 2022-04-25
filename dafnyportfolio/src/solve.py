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

default_source_for_default_args = "none"
default_args = {"Dafny": ["/infer:j", "/proverOpt:O:auto_config=false", "/proverOpt:O:type_check=true",
                          "/proverOpt:O:smt.case_split=3", "/proverOpt:O:smt.qi.eager_threshold=100",
                          "/proverOpt:O:smt.delay_units=true", "/proverOpt:O:smt.arith.solver=2"],
                "Boogie": [],
                default_source_for_default_args: []}


def determine_instance_ids(args):
    if args.only_instances is None:
        result = range(args.num_instances)
    else:
        result = set.intersection(set(range(args.num_instances)), set(args.only_instances))
    return result


def get_commit_hash():
    return args.commit_hash if args.commit_hash is not None else util.get_current_commit_hash()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run Dafny/Boogie  in a portfolio")
    parser.add_argument(metavar="PROBLEMFILE", dest="problem_file", type=str)
    parser.add_argument(metavar="PROCEDURENAME", dest="procedure_name", type=str)
    parser.add_argument(metavar="OPTIONSELECTOR", dest="option_selector_name", choices=option_selectors.keys(),
                        default=default_option_selector)
    parser.add_argument(metavar="RESULTSFILE", dest="results_filename", type=str)
    parser.add_argument("--seed", dest="seed", type=str, default="")
    parser.add_argument("--num-instances", dest="num_instances", type=int, default=cpu_count())
    parser.add_argument("--cmd", "--dafny-cmd", dest="cmd", type=str, default="dafny")
    parser.add_argument("--only-instances", dest="only_instances", type=int, nargs="*")
    parser.add_argument("--commit-hash", dest="commit_hash", type=str)
    parser.add_argument("--default-args-source", dest="default_args_source", choices=default_args.keys(),
                         default=default_source_for_default_args, help="Dafny passes additional default args to Boogie")
    args = parser.parse_args()

    chosen_option_selector = option_selectors[args.option_selector_name]
    chosen_option_selector.set_rand(Random(args.seed))
    instances = determine_instance_ids(args)
    portfolio = Portfolio(args.problem_file, args.procedure_name, args.num_instances, instances, chosen_option_selector,
                          args.cmd, default_args[args.default_args_source])

    start_time = time()
    instances_results = portfolio.run()
    end_time = time()
    portfolio_results = {"args": vars(args),
                         "commit_hash": get_commit_hash(),
                         "total_runtime": util.format_timediff(start_time, end_time),
                         "instances": instances_results}

    json.dump(portfolio_results, open(args.results_filename, "w"), indent=4, default=str)
