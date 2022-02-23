import argparse
from time import time
from multiprocessing import cpu_count
from Portfolio import *
from NoDiversificationOptionSelector import *
import util

default_option_selector = "no-diversification"
option_selectors = {
    default_option_selector: NoDiversificationOptionSelector()
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run a portfolio of SMT-Solvers")
    parser.add_argument(metavar="DAFNYFILE", dest="dafny_file", type=str)
    parser.add_argument(metavar="PROCEDURENAME", dest="procedure_name", type=str)
    parser.add_argument(metavar="OPTIONSELECTOR", dest="option_selector_name", choices=option_selectors.keys(),
                        default=default_option_selector)
    parser.add_argument(metavar="RESULTSFILE", dest="results_filename", type=str)
    parser.add_argument("--num-threads", dest="num_threads", type=int, default=cpu_count())
    args = parser.parse_args()

    start_time = time()
    portfolio = Portfolio(args.dafny_file, args.procedure_name, args.num_threads,
                          option_selectors[args.option_selector_name])
    end_time = time()
    instances_results = portfolio.run()
    portfolio_results = {"total_runtime": util.format_timediff(start_time, end_time),
                         "instances": instances_results}

    json.dump(portfolio_results, open(args.results_filename, "w"), indent=4, default=str)
