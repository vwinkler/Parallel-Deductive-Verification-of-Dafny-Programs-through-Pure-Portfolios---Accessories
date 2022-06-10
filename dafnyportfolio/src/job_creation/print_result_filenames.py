import argparse
from util import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Turn some job.json into the corresponding result filenames")
    parser.add_argument(metavar="FILE", dest="filename", type=str)
    parser.add_argument("--results-base-path", dest="results_base_path", type=str, default=".")
    args = parser.parse_args()

    for_all_calls(args.filename, lambda _, results_file: print(prepend_base_path(args.results_base_path, results_file)))
