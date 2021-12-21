from io import open
import os
import subprocess
from subprocess import PIPE
import argparse
import json
from time import time

from SmtProblem import SmtProblem
from SmtPortfolio import SmtPortfolio
from SmtProcess import SmtProcess
import util


def file_tuple(s):
    try:
        in_file, out_file = s.split(':')
        return {"in": in_file, "out": out_file}
    except:
        raise argparse.ArgumentTypeError("Problems must be FILENAME:FILENAME")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a portfolio of SMT-Solvers")
    parser.add_argument("--problems", "-f", metavar="IN_FILENAME:OUT_FILENAME", dest="filenames", type=file_tuple,
                        nargs="+")

    args = parser.parse_args()

    # simple mode:
    # Run one portfolio after the other. Each is given 4 processes. Wait for one to terminate.
    for problem_files in args.filenames:
        print("Running '{}'; writing results to '{}'...".format(problem_files["in"], problem_files["out"]))
        in_file = open(problem_files["in"], "r")
        out_file = open(problem_files["out"], "w")
        problem = SmtProblem(in_file)
        start_time = time()
        portfolio = SmtPortfolio(problem)

        processes = dict()
        instances = portfolio.make_instances(4)
        for instance in instances:
            command = instance.get_cli_command()
            process = SmtProcess(command)
            pid = process.get_pid()
            processes[pid] = (process, instance)
            print("\trunning '{}' on pid={} (total: {} processes)".format(" ".join(command), pid, len(processes)))
            instance.assign_process(process.get_stream())

        while len(processes) > 0:
            try:
                pid, _ = os.wait()
            except ChildProcessError as e:
                pid = next(iter(processes.keys()))
                (process, instance) = processes[pid]
                process.wait()

            if pid in processes:
                (process, instance) = processes[pid]
                del processes[pid]
                instance.unassign_process()
                print("\tprocess with pid={} terminated (total: {} processes remaining)".format(pid, len(processes)))

                for pid, (process, instance) in processes.items():
                    if instance.has_termination_pending():
                        process.terminate()
        end_time = time()
        result = {
            "portfolio": portfolio.get_result(),
            "total_runtime": util.format_timediff(start_time, end_time)
        }
        json.dump(result, out_file, indent=2)
