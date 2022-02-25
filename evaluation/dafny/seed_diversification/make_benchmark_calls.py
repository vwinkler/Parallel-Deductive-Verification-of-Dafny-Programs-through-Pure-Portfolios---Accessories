script = "../../../dafnyportfolio/src/solve.py"
methods_file = "methods_to_benchmark.txt"
benchmark_path_prefix = "../../../benchmarks/dafny/"
command_selection = "seed-diversification"
with open(methods_file) as file:
    for line in file.readlines():
        dfy_filename, method_name = line.split()
        cmd_template = "(set -x; python {scr} {path}{dfy} {method} {div} {dfy}.json)"
        print(cmd_template.format(scr=script, path=benchmark_path_prefix, dfy=dfy_filename, method=method_name,
                                  div=command_selection))
