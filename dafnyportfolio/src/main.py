import argparse
from Portfolio import *
from multiprocessing import cpu_count
from NoDiversificationOptionSelector import *

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
    parser.add_argument("--num-threads", dest="num_threads", type=int, default=cpu_count())
    args = parser.parse_args()

    portfolio = Portfolio(args.dafny_file, args.procedure_name, args.num_threads,
                          option_selectors[args.option_selector_name])
    portfolio.run()
