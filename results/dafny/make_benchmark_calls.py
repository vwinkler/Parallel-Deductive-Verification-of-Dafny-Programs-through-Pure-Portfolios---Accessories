import argparse

script = "../../../dafnyportfolio/src/solve.py"
methods_file = "methods_to_benchmark.txt"
benchmark_path_prefix = "../../../benchmarks/dafny/"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create calls to portfolio solver")
    parser.add_argument(metavar="OPTIONSELECTOR", dest="command_selection", type=str)
    parser.add_argument(metavar="RESULTSFILESUFFIX", dest="results_file_suffix", type=str)
    parser.add_argument(metavar="ARGS", dest="additional_args", type=str, nargs="?", default="")
    args = parser.parse_args()

    with open(methods_file) as file:
        for line in file.readlines():
            dfy_filename, method_name = line.split()
            results_filename = "{}_{}.json".format(dfy_filename, args.results_file_suffix)
            cmd_template = "(set -x; python {scr} {path}{dfy} {method} {div} {results_file} {args})"
            print(cmd_template.format(scr=script, path=benchmark_path_prefix, dfy=dfy_filename, method=method_name,
                                      div=args.command_selection, args=args.additional_args,
                                      results_file=results_filename))
