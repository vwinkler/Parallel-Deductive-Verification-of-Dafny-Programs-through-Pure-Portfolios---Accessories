import argparse
from time import time
from multiprocessing import cpu_count
from random import Random
from Portfolio import *
from NoDiversificationOptionSelector import *
from SeedDiversificationOptionSelector import *
import util

default_option_selector = "no-diversification"
option_selectors = {
    default_option_selector: NoDiversificationOptionSelector(),
    "seed-diversification": SeedDiversificationOptionSelector()
}
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the Dafny solver in a portfolio")
    parser.add_argument(metavar="DAFNYFILE", dest="dafny_file", type=str)
    parser.add_argument(metavar="PROCEDURENAME", dest="procedure_name", type=str)
    parser.add_argument(metavar="OPTIONSELECTOR", dest="option_selector_name", choices=option_selectors.keys(),
                        default=default_option_selector)
    parser.add_argument(metavar="RESULTSFILE", dest="results_filename", type=str)
    parser.add_argument("--seed", dest="seed", type=str, default="")
    parser.add_argument("--num-threads", dest="num_threads", type=int, default=cpu_count())
    parser.add_argument("--dafny-cmd", dest="dafny_command", type=str, default="dafny")
    args = parser.parse_args()

    start_time = time()
    chosen_option_selector = option_selectors[args.option_selector_name]
    chosen_option_selector.set_rand(Random(args.seed))
    portfolio = Portfolio(args.dafny_file, args.procedure_name, args.num_threads, chosen_option_selector,
                          args.dafny_command)
    end_time = time()
    instances_results = portfolio.run()
    portfolio_results = {"total_runtime": util.format_timediff(start_time, end_time),
                         "instances": instances_results}

    json.dump(portfolio_results, open(args.results_filename, "w"), indent=4, default=str)
